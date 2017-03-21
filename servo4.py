import RPi.GPIO as GPIO
from Tkinter import *
from IEILab.GroveStarterKit import Servo
from time import sleep

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, orient=HORIZONTAL,
                command=self.update)
        scale.grid(row=0)
        GPIO.setmode(GPIO.BCM)
        self.servo = Servo()
        self.servo.attach(18)

    def update(self, angle):
        self.servo.write(angle)


root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry('200x50+0+0')
root.mainloop()
GPIO.cleanup()
