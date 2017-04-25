import Serial

ser = serial.Serial('/dev/ttyACM0', 9600)
volts = []

while True:
	volts.append(float(ser.readline()))
	print ("Voltage:", volts)
