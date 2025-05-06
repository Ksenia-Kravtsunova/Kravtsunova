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

# def adc():
#     value = 0
#     measurement_time = 0  
    
#     for i in range(7, -1, -1):
#         step = 1 << i 
#         value += step
        
#         start_bit_time = time.time()
#         GPIO.output(dac, decimal2binary(value))
#         time.sleep(0.001)  
        
#         if GPIO.input(comp) == 0:
#             value -= step
        
#         measurement_time += time.time() - start_bit_time
    
#     return value, measurement_time

# try:
#     while True:
#         value, meas_time = adc()
#         voltage = value * 3.3 / 256
        
#         print(f"Цифровое значение: {value:3d}, Напряжение: {voltage:.2f}V, Время измерения: {meas_time*1000:.3f} мс")

# finally:
#     GPIO.output(dac, GPIO.LOW)
#     GPIO.output(troyka, GPIO.LOW)
#     GPIO.cleanup()

#Индусский код

def adc():
    total_time = 0
    
    start_time = time.time()
    value = 128
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 128
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 64
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 64
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 32
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 32
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 16
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 16
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 8
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 8
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 4
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 4
    total_time += time.time() - start_time
    
    start_time = time.time()
    value = 2
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 2
    total_time += time.time() - start_time
    
    start_time = time.time()
    value += 1
    GPIO.output(dac, decimal2binary(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 1
    total_time += time.time() - start_time
    
    return value, total_time

try:
    while True:
        value, meas_time = adc()
        voltage = value * 3.3 / 256
        print(f"Цифровое значение: {value:3d}, Напряжение: {voltage:.2f}V, Время измерения: {meas_time*1000:.3f} мс")
        time.sleep(0.1)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()