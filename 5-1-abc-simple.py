import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    start_time = time.time()
    for value in range(256):
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            end_time = time.time()
            measurement_time = end_time - start_time
            return value, measurement_time
    
    end_time = time.time()
    measurement_time = end_time - start_time
    return 255, measurement_time

try:
    while True:
        value, meas_time = adc()
        voltage = value * 3.3 / 256
        print(f"Цифровое значение: {value}, Напряжение: {voltage:.2f}V, Время измерения: {meas_time*1000:.3f} мс")
        time.sleep(0.1)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()