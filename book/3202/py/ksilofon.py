# encoding: utf-8
from gpiozero import Button
import pygame
pygame.init()

gumb_c1 = Button(19) # ali Button(25)
gumb_d1 = Button(13) # ali Button(24)
gumb_e1 = Button(6)  # ali Button(23)
gumb_f1 = Button(5)  # ali Button(18)
gumb_g1 = Button(22)
gumb_a1 = Button(27)
gumb_h1 = Button(17)
gumb_c2 = Button(4)

ton_c1 = pygame.mixer.Sound('c1.ogg')
ton_d1 = pygame.mixer.Sound('d1.ogg')
ton_e1 = pygame.mixer.Sound('e1.ogg')
ton_f1 = pygame.mixer.Sound('f1.ogg')
ton_g1 = pygame.mixer.Sound('g1.ogg')
ton_a1 = pygame.mixer.Sound('a1.ogg')
ton_h1 = pygame.mixer.Sound('b1.ogg')
ton_c2 = pygame.mixer.Sound('c2.ogg')

while True:
    if gumb_c1.is_pressed:
        ton_c1.play()
    if gumb_d1.is_pressed:
        ton_d1.play()
    if gumb_e1.is_pressed:
        ton_e1.play()
    if gumb_f1.is_pressed:
        ton_f1.play()
    if gumb_g1.is_pressed:
        ton_g1.play()
    if gumb_a1.is_pressed:
        ton_a1.play()
    if gumb_h1.is_pressed:
        ton_h1.play()
    if gumb_c2.is_pressed:
        ton_c2.play()
