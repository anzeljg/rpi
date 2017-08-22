# encoding: utf-8
from gpiozero import PWMLED, LightSensor
from time import sleep

led = PWMLED(27)
ldr = LightSensor(17)

while True:
    if ldr.value >= 0.75:
        led.value = 0   # ne sveti
    elif ldr.value < 0.75 and ldr.value >= 0.5:
        led.value = 0.5 # sveti na pol
    else:
        led.value = 1   # sveti
    sleep(1)
