#!/usr/bin/env python


import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

p = GPIO.PWM(4,50)
p.start(7.5)

while True:
    if RCtime(18):
        try:
            p.ChangeDutyCycle(1)
            print "ROTATE - " + RCtime(18)     # Read RC timing using pin #18
        except KeyboardInterrupt:
            GPIO.cleanup()
