import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	read_serial = ser.readline()
	volts = str(float(ser.readline()))
    amps = str(float(ser.readline()))
	print ("Voltage:",volts)
    print ("Amps:",amps)
