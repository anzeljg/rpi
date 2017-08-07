from gpiozero import Buzzer, LED
from time import sleep

def prizgi():
  zvok.on()
  aldis.on()

def ugasni():
  zvok.off()
  aldis.off()

def oddaj(zaporedje):
  for simbol in zaporedje:
    prizgi()
    if simbol == '.':
      sleep(enota)
    if simbol == '-':
      sleep(3 * enota)
    ugasni()
    sleep(enota)

zvok = Buzzer(4)
aldis = LED(27)

enota = 1 # privzeta enota je 1 sekunda

abeceda = {
  'A': '.-',     'B': '-...',   'C': '-.-.',
  'D': '-..',    'E': '.',      'F': '..-.',
  'G': '--.',    'H': '....',   'I': '..',
  'J': '.---',   'K': '-.-',    'L': '.-..',
  'M': '--',     'N': '-.',     'O': '---',
  'P': '.--.',   'Q': '--.-',   'R': '.-.',
  'S': '...',    'T': '-',      'U': '..-',
  'V': '...-',   'W': '.--',    'X': '-..-',
  'Y': '-.--',   'Z': '--..',
  '0': '-----',  '1': '.----',  '2': '..---',
  '3': '...--',  '4': '....-',  '5': '.....',
  '6': '-....',  '7': '--...',  '8': '---..',
  '9': '----.'
}

sporocilo = input('Vnesi sporoèilo:').upper()
print(sporocilo)

for znak in sporocilo:
  if znak in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
    if znak == ' ':
      sleep(7 * enota)
    else:
      oddaj(abeceda[znak])
      sleep(2 * enota)
