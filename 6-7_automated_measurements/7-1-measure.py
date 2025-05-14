import RPi.GPIO as GPIO
from time import sleep
import time
import matplotlib.pyplot as plt
from time import sleep
from time import time
def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    v = 0
    t = v + 128
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 64
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 32
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 16
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 8
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 4
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t

    t = v + 2
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t
        
    t = v + 1
    GPIO.output(dac, [int(bit) for bit in bin(t)[2:].zfill(8)])
    sleep(0.003)
    if GPIO.input(comp) == 0:
        v = t
    return v

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

l = []
down = False

time_start = time()
try:
    GPIO.output(troyka, GPIO.HIGH)
    while True:
        a = adc()
        s = round(a/256*8) * "1" + (8-round(a/256*8)) * "0"
        s = [int(i) for i in s] 
        l.append(a)
        if a >= 207:
            GPIO.output(troyka, GPIO.LOW)
            GPIO.output(troyka, 0)
            down = True
        if down and a <= 192:
            time_stop = time()
            all_time = time_stop - time_start
            data = open("data1.txt", "w")
            datatext = ""
            datatext += str(len(l)/all_time) + "\n"
            for i in l:
                datatext += str(i/256*3.3) + "\n"
            data.write(datatext)
            data.close()
            settings = open("settings1.txt", "w")
            settings.write(f"Discretisation: {len(l)/all_time} Hz\nQuantize step:{3.3/256} V")
            settings.close()

            plt.plot(l)
            plt.grid(True)
            plt.savefig("rc-plot.png")
            plt.show()
            exit()
        
        
        
            
finally:
    GPIO.output(leds + dac + [troyka], 0)

    GPIO.cleanup()
