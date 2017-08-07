from gpiozero import Button
import pygame
pygame.init()

gumb1 = Button(4)
gumb2 = Button(17)
gumb3 = Button(27)
gumb4 = Button(22)

zvok1 = pygame.mixer.Sound('crash.wav')
zvok2 = pygame.mixer.Sound('snare.wav')
zvok3 = pygame.mixer.Sound('tom.wav')
zvok4 = pygame.mixer.Sound('cowbell.wav')

gumb1.when_pressed = zvok1.play()
gumb2.when_pressed = zvok2.play()
gumb3.when_pressed = zvok3.play()
gumb4.when_pressed = zvok4.play()
