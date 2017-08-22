# encoding: utf-8
from gpiozero import Button, Buzzer

gumb = Button(22)
zvok = Buzzer(4)

while True:
    if gumb.is_pressed:
        zvok.on()
    if not gumb.is_pressed:
        zvok.off()
