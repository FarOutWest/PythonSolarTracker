import Serial

ser = serial.Serial('/dev/ttyACM0', 9600)
volts = []
#amps = []
timepoints = []

while True:
	volts.append(float(ser.readline()))
    #amps.append(float(ser.readline()))
    timepoints.append(float(ser.readline()))
	print ("Voltage:", volts)
    #print ("Amperage:", amps)
    print ("timepoints:", timepoints)
