"""
    Written By Marcus Whelan for Senior 1 project 2
    This just activates the buzzer for a short time
    this is one of the buzzer lengths 
"""
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(17,True)
time.sleep(.2)
GPIO.output(17,False)

