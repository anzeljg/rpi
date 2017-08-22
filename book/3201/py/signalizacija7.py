# encoding: utf-8
from gpiozero import LED, Button, Buzzer
from time import sleep

def prehod():
    sleep(2)
    # oranžna
    zelena.off()
    oranzna.on()
    sleep(1)
    # rdeča
    oranzna.off()
    rdeca.on()
    sleep(0.5)
    # zelena za pešce
    rdeca2.off()
    zelena2.on()
    zvok.on()
    sleep(2)
    # rdeča za pešce
    zvok.off()
    zelena2.off()
    sleep(0.5)
    # rdeča in oranžna
    rdeca2.on()
    oranzna.on()
    sleep(1)
    # zelena
    rdeca.off()
    oranzna.off()
    zelena.on()

# semafor za avtomobile
zelena = LED(17)
rdeca = LED(22)
oranzna = LED(27)

# semafor za pešce
zelena2 = LED(19)
rdeca2 = LED(26)

# gumb za pešce
gumb = Button(24)

# piezo aktivni brenčač
zvok = Buzzer(18)

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
