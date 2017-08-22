# encoding: utf-8
from gpiozero import LED
from time import sleep

zelena = LED(19)
rdeca = LED(26)

while True:
    rdeca.on()
    zelena.off()
    sleep(3)
    rdeca.off()
    zelena.on()
    sleep(1)
