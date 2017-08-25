# encoding: utf-8
import gpiozero
import random
import time

led = [
    gpiozero.LED(4),  # modra
    gpiozero.LED(18), # rdeča
    gpiozero.LED(22), # oranžna
    gpiozero.LED(23)  # zelena
]

# Ustvarjaj zaporedno dodajanje različnih/naključnih barv v zaporedje,
# ki je najprej dolgo 1 barvo, na koncu pa 10 barv. Izpši zaporedje oz.
# prižigaj lučke v zaporedju.
zaporedje = []
for i in range(10):
    nova = random.randint(0, 3)
    zaporedje.append(nova)
    # izpiši zaporedje
    print(zaporedje)
    # prižigaj lučke v zaporedju
    for barva in zaporedje:
        led[barva].on()
        time.sleep(1)
        led[barva].off()
        time.sleep(0.2)
    time.sleep(2)
