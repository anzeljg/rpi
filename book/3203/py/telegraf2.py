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

gumb.when_pressed = prizgi()
gumb.when_released = ugasni()
