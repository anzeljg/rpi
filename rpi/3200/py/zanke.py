# encoding: utf-8
import gpiozero
import time

pin17 = gpiozero.PWMLED(17)

while True: # zanka, ki zagotovi ponavljanje kode v nedogled
    svetilnost = 0
    while svetilnost < 1:
        svetilnost = round(svetilnost, 1)
        pin17.value = svetilnost
        svetilnost = svetilnost + 0.1
        time.sleep(0.5)
    while svetilnost > 0.1:
        svetilnost = round(svetilnost, 1)
        pin17.value = svetilnost
        svetilnost = svetilnost - 0.1
        time.sleep(0.5)
