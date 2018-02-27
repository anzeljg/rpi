# encoding: utf-8
import gpiozero

gumb = gpiozero.Button(22)
zvok = gpiozero.Buzzer(4)

while True:
    if gumb.is_pressed:
        zvok.on()
    if not gumb.is_pressed:
        zvok.off()
