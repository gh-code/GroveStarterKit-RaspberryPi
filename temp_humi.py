import RPi.GPIO as GPIO
from IEILab.GroveStarterKit import DHT
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dht = DHT(18)
dht.begin()
while True:
    data = dht.readHT()
    if data:
        t, h = data
        print '------------------------------'
        print 'temperature = {:.1f}'.format(t)
        print 'humidity = {:.1f}%'.format(h)
    sleep(2)
