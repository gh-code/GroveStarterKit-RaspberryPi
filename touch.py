import RPi.GPIO as GPIO
from IEILab.GroveStarterKit import TouchSensor
from time import sleep

PIN = 18

GPIO.setmode(GPIO.BCM)
touch = TouchSensor()
touch.attach(PIN)

try:
    while True:
        print 'Touched' if touch.isTouched() else ''
        sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
