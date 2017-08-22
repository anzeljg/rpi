# encoding: utf-8
from gpiozero import LED, Button, Buzzer
from time import sleep

led1 = LED(17)
led2 = LED(22)
led3 = LED(27)

led4 = LED(19)
led5 = LED(26)

led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
