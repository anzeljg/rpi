# encoding: utf-8
import gpiozero
import time

led1 = gpiozero.LED(26)
led2 = gpiozero.LED(19)
led3 = gpiozero.LED(22)
led4 = gpiozero.LED(27)
led5 = gpiozero.LED(17)

# poskrbimo, da so vse LED diode ugasnjene
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()

while True:
    led5.off()
    led1.on()
    time.sleep(1)

    led1.off()
    led2.on()
    time.sleep(1)

    led2.off()
    led3.on()
    time.sleep(1)

    led3.off()
    led4.on()
    time.sleep(1)

    led4.off()
    led5.on()
    time.sleep(1)
