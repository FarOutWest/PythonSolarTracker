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

    s1 = int(GetReadingFromSensor(1))
    s2 = int(GetReadingFromSensor(2))
    s3 = int(GetReadingFromSensor(3))
    s4 = int(GetReadingFromSensor(4))

    if  s1 + s2 < s4 + s3:
        try:
            topServo.start(1)
            
            print ("UP")
        except KeyboardInterrupt:
	    print("")
	
    else:
        try:
            topServo.start(40)
            
            print ("DOWN")
        except KeyboardInterrupt:
            print("")

    if s1 +s4 < s2 + s3:
        try:
            print ("LEFT")
            botServo.start(1)
            

        except KeyboardInterrupt:
            print("")

    else:
        try:
            print ("RIGHT")
            botServo.start(40)
	    
        except KeyboardInterrupt:
            print("")

    time.sleep(.1)
    topServo.stop()
    botServo.stop()

    time.sleep(5)


GPIO.cleanup()
