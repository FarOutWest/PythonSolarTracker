import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
volts = []
amps = []

#goes in start function code from light-sensor-to-servo-reading.py
while True:
    volts.append(float(ser.readline()))
    amps.append(float(ser.readline()))
    print ("Voltage:", volts)
    print ("Amperage:", amps)
