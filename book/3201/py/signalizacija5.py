# encoding: utf-8
from gpiozero import LED
from time import sleep

zelena = LED(17)
rdeca = LED(22)
oranzna = LED(27)

while True:
    rdeca.on()
    oranzna.off()
    zelena.off()
    sleep(3)
    oranzna.on()
    sleep(1)
    rdeca.off()
    oranzna.off()
    zelena.on()
    sleep(3)
    oranzna.on()
    zelena.off()
    sleep(1)
