# encoding: utf-8
import gpiozero
import time

def prizgi():
    aldis.on()
    zvok.on()

def ugasni():
    aldis.off()
    zvok.off()

def oddaj(zaporedje):
    for znak in zaporedje:
        prizgi()
        if znak == '.':
            time.sleep(enota)
        if znak == '-':
            time.sleep(3 * enota)
        ugasni()
        time.sleep(enota)

zvok = gpiozero.Buzzer(4)
aldis = gpiozero.LED(27)

enota = 0.1 # privzeta enota je desetinka sekunde

abeceda = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   '0': '-----',
    '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',
    '7': '--...',  '8': '---..',  '9': '----.'
}

sporocilo = input('Vnesi sporočilo:').upper()
sporocilo = sporocilo.replace('Č', 'C')
sporocilo = sporocilo.replace('Š', 'S')
sporocilo = sporocilo.replace('Ž', 'Z')

for znak in sporocilo:
    if znak in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
        if znak == ' ':
            time.sleep(7 * enota)
        else:
            oddaj(abeceda[znak])
            time.sleep(2 * enota)
