# encoding: utf-8
import tm1637
import time

prikaz = tm1637.TM1637(3, 2)

# Prikazuje napise nivojev v zaporedju od 1 do 20.
# Prototip napisa za 1. nivo izgleda takole: nI:01

prikaz.clear()

for i in range(1, 21):
    D = i // 10 # desetice
    E = i % 10  # enice
    prikaz.set_values(['n', 'I', D, E])
    prikaz.set_doublepoint(True)
    time.sleep(1)

# Kadar igralec izgubi: buuu
prikaz.set_doublepoint(False)
prikaz.set_values(['b', 'u', 'u', 'u'])
time.sleep(1)

# Kadar igralec zmaga: JAAA
prikaz.set_doublepoint(False)
prikaz.set_values(['J', 'A', 'A', 'A'])
time.sleep(1)

prikaz.clear()
prikaz.cleanup()
