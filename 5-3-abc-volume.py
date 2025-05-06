import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def adc():
    j = 128
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14)==1:
        j -= 64
    else:
        j += 64
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1 :
        j -= 32
    else:
        j += 32
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1:
        j -= 16
    else:
        j += 16
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1:
        j -= 8
    else:
        j += 8
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1:
        j -= 4
    else:
        j += 4
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1:
        j -= 2
    else:
        j += 2
    GPIO.output(dac, [int (elem) for elem in bin(j)[2:].zfill(8)])
    sleep(0.01)
    if GPIO.input(14) == 1:
        j -= 1
    else:
        j += 1
    if GPIO.input(14) == 1:
        j -= 1

    return j

def volume(n):
    n = int(n/256*10)
    spisok = [0]*8
    for i in range(n-1):
        spisok[i] = 1
    return spisok

try:
    while True:
        i = adc()
        if i!=0:
            GPIO.output(leds, volume(i))
            print(int(i/256*10))
             
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()