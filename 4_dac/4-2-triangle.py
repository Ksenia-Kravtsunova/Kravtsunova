import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6] 
GPIO.setup(dac, GPIO.OUT) 

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    period = float(input("Введите период треугольного сигнала: "))
    if period <= 0:
        raise ValueError("Период должен быть положительным числом")
    
    delay = period / 510  
    while True:
        for value in range(256):
            GPIO.output(dac, dec2bin(value))
            time.sleep(delay)
        
        for value in range(254, 0, -1):
            GPIO.output(dac, dec2bin(value))
            time.sleep(delay)

except ValueError as e:
    print(f"Ошибка ввода: {e}")
except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем")
finally:
    GPIO.output(dac, 0)  
    GPIO.cleanup() 
    print("Программа завершена")