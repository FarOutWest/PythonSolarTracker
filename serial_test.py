import serial

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_serial = ser.readline()
	value = str(int (ser.readline(),16))
	print value
	print read_serial
