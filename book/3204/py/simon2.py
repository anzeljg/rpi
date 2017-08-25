# encoding: utf-8
import gpiozero
import pygame
import time
pygame.init()

def predvajaj(i):
    led[i].on()
    zvok[i].play()
    time.sleep(1)
    led[i].off()

led = [
    gpiozero.LED(4),  # modra
    gpiozero.LED(18), # rdeča
    gpiozero.LED(22), # oranžna
    gpiozero.LED(23)  # zelena
]

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


while True:
    if gumb[0].is_pressed:
        predvajaj(0)
    if gumb[1].is_pressed:
        predvajaj(1)
    if gumb[2].is_pressed:
        predvajaj(2)
    if gumb[3].is_pressed:
        predvajaj(3)
