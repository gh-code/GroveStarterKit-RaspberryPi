import RPi.GPIO as GPIO
from IEILab.GroveStarterKit import LEDBar
from time import sleep

clk = 23
dta = 18

GPIO.setmode(GPIO.BCM)
ledBar = LEDBar(clk, dta)

for level in range(11):
    ledBar.setLevelReverse(level)
    sleep(0.1)

for level in range(11):
    ledBar.setLevel(level)
    sleep(0.1)

for level in range(10, -1, -1):
    ledBar.setLevel(level)
    sleep(0.1)

for num in range(11):
    ledBar.singleLed(num, True)
    if num > 0:
        ledBar.singleLed(num - 1, False)
    sleep(0.1)

GPIO.cleanup()
