# encoding: utf-8
import gpiozero
import time

led = gpiozero.PWMLED(27)
ldr = gpiozero.LightSensor(17)

while True:
    if ldr.value >= 0.75:
        led.value = 0   # ne sveti
    elif ldr.value < 0.75 and ldr.value >= 0.5:
        led.value = 0.5 # sveti na pol
    else:
        led.value = 1   # sveti
    time.sleep(1)
