# encoding: utf-8
import gpiozero

zvok = gpiozero.Buzzer(4)
aldis = gpiozero.LED(27)

zvok.off()
aldis.off()
