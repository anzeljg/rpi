# encoding: utf-8
import gpiozero

gumb = gpiozeroButton(22)
zvok = gpiozero.Buzzer(4)
aldis = gpiozero.LED(27)

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
