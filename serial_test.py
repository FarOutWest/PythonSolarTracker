import serial

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_serial = ser.readline()
	value = str(float(ser.readline()))
	print ("Voltage:",value)
