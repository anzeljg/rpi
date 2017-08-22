# encoding: utf-8
from gpiozero import LED
from time import sleep

led1 = LED(26)
led2 = LED(19)
led3 = LED(22)
led4 = LED(27)
led5 = LED(17)

# poskrbimo, da so vse LED diode ugasnjene
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()

while True:
    led5.off()
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    led3.on()
    sleep(1)
    led3.off()
    led4.on()
    sleep(1)
    led4.off()
    led5.on()
    sleep(1)
