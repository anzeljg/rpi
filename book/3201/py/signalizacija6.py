from gpiozero import LED
from time import sleep

# semafor za avtomobile
zelena = LED(17)
rdeca = LED(22)
oranzna = LED(27)

# semafor za pešce
zelena2 = LED(19)
rdeca2 = LED(26)

while True:
    rdeca.on()
	oranzna.off()
    zelena.off()
	zelena2.on()
	rdeca2.off()
    sleep(3)
	oranzna.on()
	zelena2.off()
	rdeca2.on()
	sleep(1)
	rdeca.off()
	oranzna.off()
	zelena.on()
	sleep(3)
	oranzna.on()
    zelena.off()
    sleep(1)
