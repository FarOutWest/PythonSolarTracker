import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	volts = str(float(ser.readline()))
    amps = str(float(ser.readline()))
	print ("Voltage:", volts)
    print ("Amps:", amps)
