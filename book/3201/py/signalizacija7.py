from gpiozero import LED, Button, Buzzer
from time import sleep

def prehod():
    sleep(3)
	zelena.off()
	oranzna.on()
	sleep(1)
	oranzna.off()
	rdeca.on()
	rdeca2.off()
	zelena2.on()
	zvok.on()
	sleep(3)
	zvok.off()
	zelena2.off()
	rdeca2.on()
	oranzna.on()
	sleep(1)
	rdeca.off()
	oranzna.off()
	zelena.on()

# semafor za avtomobile
zelena = LED(17)
rdeca = LED(22)
oranzna = LED(27)

# semafor za pe�ce
zelena2 = LED(19)
rdeca2 = LED(26)

# gumb za pe�ce
gumb = Button(24)

# piezo aktivni bren�a�
zvok = Buzzer(5)

# zelena za avtomobile, rde�a za pe�ce
rdeca.off()
oranzna.off()
zelena.on()
rdeca2.on()
zelena2.off()

# ko pe�ec pritisne gumb
gumb.when_pressed = prehod()
