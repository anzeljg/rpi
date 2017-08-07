from gpiozero import Button
import pygame
pygame.init()

gumb = Button(22)
zvonec = pygame.mixer.Sound('doorbell.wav')

gumb.when_pressed = zvonec.play()
