# encoding: utf-8
import gpiozero
import random
import tm1637
import time
import pygame
pygame.init()


led = [
    gpiozero.LED(4),  # modra
    gpiozero.LED(18), # rdeča
    gpiozero.LED(22), # oranžna
    gpiozero.LED(23)  # zelena
]

start = gpiozero.Button(26) # gumb za začetek igre
gumb = [
    gpiozero.Button(13), # modra
    gpiozero.Button(16), # rdeča
    gpiozero.Button(19), # oranžna
    gpiozero.Button(20)  # zelena
]

zvok = [
    pygame.mixer.Sound('blue.ogg'),   # modra
    pygame.mixer.Sound('red.ogg'),    # rdeča
    pygame.mixer.Sound('orange.ogg'), # oranžna
    pygame.mixer.Sound('green.ogg')   # zelena
]

prikaz = tm1637.TM1637(3, 2)


zaporedje = []
nivo = 0


def predvajaj(i):
    led[i].on()
    zvok[i].play()
    time.sleep(1)
    led[i].off()

def konec_igre():
    prikaz.set_values(['b', 'u', 'u', 'u'])
    prikaz.set_doublepoint(False)
    time.sleep(3)
    prikaz.clear()
    raise SystemExit # nemudoma konča program

def nova_igra():
    zaporedje = []  # sprazni zaporedje lučk
    prikaz.clear()  # prikazovalni ne kaže nič

    # največ koliko nivojev mora igralec ponoviti,
    # da zmaga
    nivoji = 20
    for nivo in range(nivoji):
        time.sleep(1)
        nov_nivo()
        igralec_ponovi_nivo()

    # zmaga igralca
    prikaz.set_doublepoint(False)
    prikaz.set_values(['J', 'A', 'A', 'A'])
    time.sleep(3)
    prikaz.clear()
    

def nov_nivo():
    global nivo, prikaz
    nivo = nivo + 1
    # izpiši nivo
    D = nivo // 10 # desetice
    E = nivo % 10  # enice
    prikaz.set_values(['n', 'I', D, E])
    prikaz.set_doublepoint(True)
    # ustvari novo naključno lučko
    poteza = random.randint(0, 3)
    zaporedje.append(poteza)
    # prižigaj lučke in predvajaj zvoke v zaporedju
    for barva in zaporedje:
        led[barva].on()
        zvok[barva].play()
        time.sleep(1)
        led[barva].off()
        time.sleep(0.2)


def igralec_ponovi_nivo():
    poteza = 0
    while poteza < len(zaporedje):
        # za vsako potezo ima igralec na voljo
        # 5 sekund = 50 x 0.1 sekunde
        for korak in range(50):
            #print(korak)
            # modra
            if gumb[0].is_pressed:
                predvajaj(0)
                if zaporedje[poteza] != 0:
                    konec_igre()
                poteza = poteza + 1
                break
            # rdeča
            if gumb[1].is_pressed:
                predvajaj(1)
                if zaporedje[poteza] != 1:
                    konec_igre()
                poteza = poteza + 1
                break
            # oranžna
            if gumb[2].is_pressed:
                predvajaj(2)
                if zaporedje[poteza] != 2:
                    konec_igre()
                poteza = poteza + 1
                break
            # zelena
            if gumb[3].is_pressed:
                predvajaj(3)
                if zaporedje[poteza] != 3:
                    konec_igre()
                poteza = poteza + 1
                break
            time.sleep(0.1)


prikaz.clear()
while True:
    if start.is_pressed:
        nova_igra()
