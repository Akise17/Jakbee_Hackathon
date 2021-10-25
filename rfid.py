#!/usr/bin/env python

#import RPi.GPIO as GPIO
from Editablemfrc522 import SimpleMFRC522
import os
import time
import threading

reader = SimpleMFRC522()

Timer = 3

#try:
def readRfid():
    id = reader.read_id()
    return id

def init_timer():
    return

def servoClose():
    os.system("python /home/pi/Documents/Igy/servo.py")
    timer.cancel()
    
timer = threading.Timer(Timer, init_timer)
timer.cancel()

while True:
    text = readRfid()
    print(text)
    if(str(text) == "277385552384"):
        os.system("python /home/pi/Documents/Igy/servoOpen.py")
        timer = threading.Timer(Timer, servoClose)
        timer.start();
#finally:
#        GPIO.cleanup()