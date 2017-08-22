# encoding: utf-8
from gpiozero import Button
import pygame
pygame.init()

gumb1 = Button(4)
gumb2 = Button(17)
gumb3 = Button(27)
gumb4 = Button(22)

zvok1 = pygame.mixer.Sound('crash.ogg')
zvok2 = pygame.mixer.Sound('snare.ogg')
zvok3 = pygame.mixer.Sound('tom.ogg')
zvok4 = pygame.mixer.Sound('cowbell.ogg')

while True:
    if gumb1.is_pressed:
        zvok1.play()
    if gumb2.is_pressed:
        zvok2.play()
    if gumb3.is_pressed:
        zvok3.play()
    if gumb4.is_pressed:
        zvok4.play()
