# encoding: utf-8
from gpiozero import Button, Buzzer, LED

gumb = Button(22)
zvok = Buzzer(4)
aldis = LED(27)

def prizgi():
    zvok.on()
    aldis.on()

def ugasni():
    zvok.off()
    aldis.off()

while True:
    if gumb.is_pressed:
        prizgi()
    if not gumb.is_pressed:
        ugasni()

