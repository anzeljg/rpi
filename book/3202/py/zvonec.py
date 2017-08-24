# encoding: utf-8
import gpiozero
import pygame
pygame.init()

gumb = gpiozero.Button(22)
zvonec = pygame.mixer.Sound('doorbell.ogg')

while True:
    if gumb.is_pressed:
        zvonec.play()
