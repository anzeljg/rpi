# encoding: utf-8
import gpiozero
import time

def prizgi():
    aldis.on()
    zvok.on()

def ugasni():
    aldis.off()
    zvok.off()

zvok = gpiozero.Buzzer(4)
aldis = gpiozero.LED(27)

enota = 0.1 # privzeta enota je desetinka sekunde

while True:
    for znak in '...---...':
        prizgi()
        if znak == '.':
            time.sleep(enota)
        if znak == '-':
            time.sleep(3 * enota)
        ugasni()
        time.sleep(enota)
    time.sleep(2 * enota)
