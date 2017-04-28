import time
import wiringpi

wiringpi.wiringPiSetupGpio()

#set pins 18 & 12 to pwm output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(12, wiringpi.GPIO.PWM_OUTPUT)

#set up pin 'X' for ldr input
wiringpi.pinMode('X', wiringpi.GPIO.INPUT)

#set the PWM mode to milliseconds
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

#setup ldr pins
TopLeft = 0;
TopRight = 1;
BottomLeft = 2;
BottomRight = 3;

#read the values from the ldr pins
dtime = wiringpi.Read(12)/20
tol = wiringpi.Read('X')/4

#find the average top, bottom, left, and right values
avgTop = (TopLeft + TopRight) / 2
avgBottom = (BottomRight + BottomLeft) / 2
avgLeft = (TopLeft + BottomLeft) / 2
avgRight = (TopRight + BottomRight) / 2

#check the difference of up/down and left/right
diffVert = avgTop - avgBottom
diffHoriz = avgLeft - avgRight

#check if the difference is in the tolerance else change vertical angle
if (-1*tol > diffVert || diffVert > tol):
    if (avgTop > avgBottom):
        wiringpi.pwmWrite(12, -=1)
        if (wiringpi.Read(12) > 180):
            wiringpi.pwmWrite(12, 180)
    else:
        wiringpi.pwmWrite(12, +=1)
        if (wiringpi.Read(12) < 0):
            wiringpi.pwmWrite(12, 0)

#same for horizontal
