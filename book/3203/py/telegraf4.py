# encoding: utf-8
from gpiozero import Buzzer, LED
from time import sleep

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
            sleep(enota)
        if znak == '-':
            sleep(3 * enota)
        ugasni()
        sleep(enota)

zvok = Buzzer(4)
aldis = LED(27)

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
    '7': '--...',  '8': '---..',  '9': '----.',
    'Č': '-..-',   'Š': '----',   'Ž': '.--'
}

sporocilo = input('Vnesi sporočilo:').upper()

for znak in sporocilo:
    if znak in 'ABCDEFGHIJKLMNOPQRSTUVWXYZČŠŽ0123456789 ':
        if znak == ' ':
            sleep(7 * enota)
        else:
            oddaj(abeceda[znak])
            sleep(2 * enota)
