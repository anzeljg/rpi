# encoding: utf-8
import gpiozero
import time

# semafor za avtomobile
zelena = gpiozero.LED(17)
rdeca = gpiozero.LED(22)
oranzna = gpiozero.LED(27)

# semafor za pešce
zelena2 = gpiozero.LED(19)
rdeca2 = gpiozero.LED(26)

while True:
    rdeca.on()
    oranzna.off()
    zelena.off()
    zelena2.on()
    rdeca2.off()
    time.sleep(3)

    oranzna.on()
    zelena2.off()
    rdeca2.on()
    time.sleep(1)

    rdeca.off()
    oranzna.off()
    zelena.on()
    time.sleep(3)

    oranzna.on()
    zelena.off()
    time.sleep(1)
