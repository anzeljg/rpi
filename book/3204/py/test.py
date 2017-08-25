import tm1637
import time

disp = tm1637.TM1637(3, 2)

disp.set_values(['A', 'B', 'b', 'C'])
time.sleep(3)

disp.set_values(['c', 'D', 'd', 'E'])
time.sleep(3)

disp.set_values(['F', 'G', 'H', 'h'])
time.sleep(3)

disp.set_values(['I', 'J', 'K', 'L'])
time.sleep(3)

disp.set_values(['l', 'n', 'O', 'o'])
time.sleep(3)

disp.set_values(['P', 'r', 'S', 'U'])
time.sleep(3)

disp.set_values(['Y', 'Z', ' ', ' '])
time.sleep(3)

disp.set_values(['T1', 'T2', 'W1', 'W2'])
time.sleep(3)

disp.set_value('M1', 0)
time.sleep(3)

disp.set_value('M2', 1)
time.sleep(3)

disp.set_values(range(4))
time.sleep(3)

disp.set_values(range(4, 8))
time.sleep(3)

disp.set_values(range(6, 10))
time.sleep(3)

x = True
for i in range(8):
    disp.set_doublepoint(x)
    disp.set_brightness(i)
    time.sleep(3)
    x = not x

disp.clear()

disp.cleanup()
