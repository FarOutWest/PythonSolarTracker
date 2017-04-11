#!/usr/bin/env python

# servo.py
# 2015-05-20
# Public Domain

import time

import pigpio

SERVO = [4, 11, 18]     # Servos connected to gpios 4, 11, 18
DIR   = [1, -1, 1]
PW    = [1500, 1500, 1500]
SPEED = [50, 100, 150]


pi = pigpio.pi() # Connect to local Pi.

for x in SERVO:
   pi.set_mode(x, pigpio.OUTPUT) # Set gpio as an output.

start = time.time()

while (time.time() - start) < 60: # Spin for 60 seconds.

   for x in range (len(SERVO)): # For each servo.

      print("Servo {} pulsewidth {} microseconds.".format(x, PW[x]))

      pi.set_servo_pulsewidth(SERVO[x], PW[x])

      PW[x] += (DIR[x] * SPEED[x])

      if (PW[x] < 1100) or (PW[x] > 1900): # Bounce back at safe limits.
         DIR[x] = - DIR[x]

      time.sleep(0.5)

for x in SERVO:
   pi.set_servo_pulsewidth(x, 0) # Switch servo pulses off.

pi.stop()
