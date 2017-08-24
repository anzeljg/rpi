# encoding: utf-8
import gpiozero
import time

def prehod():
    time.sleep(2)
    # oranžna
    zelena.off()
    oranzna.on()
    time.sleep(1)
    # rdeča
    oranzna.off()
    rdeca.on()
    time.sleep(0.5)
    # zelena za pešce
    rdeca2.off()
    zelena2.on()
    zvok.on()
    time.sleep(2)
    # rdeča za pešce
    zvok.off()
    zelena2.off()
    time.sleep(0.5)
    # rdeča in oranžna
    rdeca2.on()
    oranzna.on()
    time.sleep(1)
    # zelena
    rdeca.off()
    oranzna.off()
    zelena.on()

# semafor za avtomobile
zelena = gpiozero.LED(17)
rdeca = gpiozero.LED(22)
oranzna = gpiozero.LED(27)

# semafor za pešce
zelena2 = gpiozero.LED(19)
rdeca2 = gpiozero.LED(26)

# gumb za pešce
gumb = gpiozero.Button(24)

# piezo aktivni brenčač
zvok = gpiozero.Buzzer(18)

# zelena za avtomobile, rdeča za pešce
rdeca.off()
oranzna.off()
zelena.on()
rdeca2.on()
zelena2.off()

# vsakokrat ko pešec pritisne gumb
while True:
    if gumb.is_pressed:
        prehod()
