from gpiozero import Button, Buzzer

gumb = Button(22)
zvok = Buzzer(4)

gumb.when_pressed = zvok.on()
gumb.when_released = zvok.off()
