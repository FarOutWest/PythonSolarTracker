import Serial

ser = serial.Serial('/dev/ttyACM0', 9600)
volts = []
amps = []


while True:
	volts.append(float(ser.readline()))
    amps.append(float(ser.readline()))
	print ("Voltage:", volts)
    print ("Amperage:", amps)
