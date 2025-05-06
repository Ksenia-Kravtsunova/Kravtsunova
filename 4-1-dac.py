import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def bina(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        user_input = input('Введите число от 0 до 255: ')
        if user_input.lower() == 'q':
            break

        try:
            number = float(user_input)
                    
            if number % 1 != 0:
                print('Ошибка: введено не целое число')
                continue
            
            number = int(number)
            if number < 0:
                print("Ошибка: введено отрицательное число")
                continue

            if number > 255:
                print("Ошибка: число превышает 255")
                continue    

        except ValueError:
            print('Ошибка: введено не числовое значение')   
            continue

        binary_value = bina(number)
        GPIO.output(dac, binary_value)
            
        voltage = (number / 255.0) * 3.3
        print(f"Предполагаемое напряжение: {voltage:.2f} В")
  
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()