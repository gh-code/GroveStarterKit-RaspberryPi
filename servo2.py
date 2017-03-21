import RPi.GPIO as GPIO
from IEILab.GroveStarterKit import Servo
from time import sleep

try:
    GPIO.setmode(GPIO.BCM)
    s = Servo()
    s.attach(18)    # PCM_CLK pin in BCM mode
    for angle in range(0, 181, 10):
        s.write(angle)
        print s.read()
        sleep(1)
except ValueError as e:
    print 'Error: ', e
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

