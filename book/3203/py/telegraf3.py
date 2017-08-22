# encoding: utf-8
from gpiozero import Buzzer, LED
from time import sleep

def prizgi():
    aldis.on()
    zvok.on()

def ugasni():
    aldis.off()
    zvok.off()

zvok = Buzzer(4)
aldis = LED(27)

enota = 0.1 # privzeta enota je desetinka sekunde

while True:
    for znak in '...---...':
        prizgi()
        if znak == '.':
            sleep(enota)
        if znak == '-':
            sleep(3 * enota)
        ugasni()
        sleep(enota)
    sleep(2 * enota)
