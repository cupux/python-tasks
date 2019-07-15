from gpiozero import LED, Button
from time import sleep
from signal import pause

red = LED(17)
green = LED(14)
yellow = LED(15)
button = Button(18)
while True:
    red.on()
    sleep(1)
    red.off()
    green.on()
    sleep(1)
    green.off()
    yellow.on()
    sleep(1)
    yellow.off()
