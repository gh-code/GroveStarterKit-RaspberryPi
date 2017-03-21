import RPi.GPIO as GPIO
from IEILab.GroveStarterKit import Servo
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

s = Servo()
s.attach(18)    # PCM_CLK pin in BCM mode

s.write(0)
sleep(1)
s.write(180)
sleep(1)
