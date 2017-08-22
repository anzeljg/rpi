# encoding: utf-8
from gpiozero import Buzzer, LED
from time import sleep

zvok = Buzzer(4)
aldis = LED(27)

zvok.off()
aldis.off()
