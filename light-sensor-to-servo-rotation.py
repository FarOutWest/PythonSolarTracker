#!/usr/bin/env python


import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


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

def GetReadingFromSensor(sensor):
        if sensor == 1: value = RCtime(27)
        elif sensor == 2: value = RCtime(16)
        elif sensor == 3: value = RCtime(5)
        elif sensor == 4: value = RCtime(26)
        else: value = null

        if value > 50000:
            value = 50000

        print str(sensor) + " " + str(value)

        return value


topServo = GPIO.PWM(4,100)
botServo = GPIO.PWM(12,100)
topServo.start(0)
botServo.start(0)

while True:

    s1 = GetReadingFromSensor(1)
    s2 = GetReadingFromSensor(2)
    s3 = GetReadingFromSensor(3)
    s4 = GetReadingFromSensor(4)
    maxDif = 5000

    if  (s1 - s4) < (-maxDif) or (s2 - s3) < (-maxDif):
        try:
            topServo.ChangeDutyCycle(1)
            time.sleep(.01)
	    topServo.ChangeDutyCycle(0)

            print ("UP")
        except KeyboardInterrupt:
	    print("")

    elif (s1 - s4) > maxDif or (s2 - s3) > maxDif:
        try:
            topServo.ChangeDutyCycle(40)
	    time.sleep(.03)
            topServo.ChangeDutyCycle(0)

            print ("DOWN")
        except KeyboardInterrupt:
            print("")

    if (s1 - s2) < (-maxDif) or (s4 -s3) < (-maxDif):
        try:
            print ("RIGHT")
            botServo.ChangeDutyCycle(40)
	    time.sleep(.01)
            botServo.ChangeDutyCycle(0)

        except KeyboardInterrupt:
            print("")

    elif (s1 - s2) > maxDif or (s4  - s3) > maxDif:
        try:
            print ("LEFT")
            botServo.ChangeDutyCycle(1)
            time.sleep(.03)
            botServo.ChangeDutyCycle(0)


        except KeyboardInterrupt:
            print("")


    time.sleep(5)


GPIO.cleanup()
