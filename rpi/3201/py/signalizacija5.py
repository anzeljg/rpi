# encoding: utf-8
import gpiozero
import time

zelena = gpiozero.LED(17)
rdeca = gpiozero.LED(22)
oranzna = gpiozero.LED(27)

while True:
    rdeca.on()
    oranzna.off()
    zelena.off()
    time.sleep(3)

    oranzna.on()
    time.sleep(1)

    rdeca.off()
    oranzna.off()
    zelena.on()
    time.sleep(3)

    oranzna.on()
    zelena.off()
    time.sleep(1)
