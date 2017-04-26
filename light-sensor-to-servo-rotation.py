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
        if sensor == 1: value = str(RCtime(27))
        elif sensor == 2: value = str(RCtime(16))
        elif sensor == 3: value = str(RCtime(5))
        elif sensor == 4: value = str(RCtime(26))
        else: value = "null"

        print value

        return value


topServo = GPIO.PWM(4,50)
botServo = GPIO.PWM(12,50)
while True:
    s1 = GetReadingFromSensor(27)
    s2 = GetReadingFromSensor(16)
    s3 = GetReadingFromSensor(5)
    s4 = GetReadingFromSensor(26)


    if  s1 > s2:
        try:
            topServo.start(1)
            print ("UP")
        except KeyboardInterrupt:
            GPIO.cleanup()

    elif  s1 < s2:
        try:
            topServo.start(1)
            print ("DOWN")
        except KeyboardInterrupt:
            GPIO.cleanup()


    if s1 > s4:
        try:
            print ("LEFT")
            botServo.start(1)

        except KeyboardInterrupt:
            GPIO.cleanup()

    elif s1 < s4:
        try:
            print ("RIGHT")
            botServo.start(1)
        except KeyboardInterrupt:
            GPIO.cleanup()

    topServo.stop()
    botServo.stop()



    print (GetReadingFromSensor(1))
    print (GetReadingFromSensor(2))
    print (GetReadingFromSensor(3))
    print (GetReadingFromSensor(4))

    time.sleep(5)


GPIO.cleanup()
