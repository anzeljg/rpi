# encoding: utf-8
from gpiozero import Button
import pygame
pygame.init()

gumb = Button(22)
zvonec = pygame.mixer.Sound('doorbell.ogg')

while True:
    if gumb.is_pressed:
        zvonec.play()
