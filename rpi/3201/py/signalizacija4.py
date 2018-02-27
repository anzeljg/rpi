# encoding: utf-8
import gpiozero
import time

zelena = gpiozero.LED(19)
rdeca = gpiozero.LED(26)

while True:
    rdeca.on()
    zelena.off()
    time.sleep(3)

    rdeca.off()
    zelena.on()
    time.sleep(1)
