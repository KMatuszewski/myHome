import time
import serial
import sys
from datetime import datetime

time.sleep(10)

RS232_0 = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=2400,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)


RS232_1 = serial.Serial(
	port='/dev/ttyUSB1',
	baudrate=2400,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

sys.stdout = open("/home/pi/buderus/output.txt", "a+")
print ("test sys.stdout")

counter=0
print('----------------------------------------------------')
print(datetime.now())
print(RS232_0.name)
print(RS232_1.name)
if RS232_0.isOpen():
	print('Port ' + RS232_0.name + ' is open ...')
else:
	print('Port ' + RS232_0.name + ' is closed ...')
if RS232_1.isOpen():
	print('Port ' + RS232_1.name + ' is open ...')
else:
	print('Port ' + RS232_1.name + ' is closed ...')

print('----------------------------------------------------')
print(' ')


RS232_0.flushInput()
RS232_0.flushOutput()
RS232_1.flushInput()
RS232_1.flushOutput()


while 1:
	resp = RS232_0.read(1)
        resp_l = len(resp)
	print (str(datetime.now()) + ' - dane1 = ' + str(resp_l))
		
	if len(resp)>0:
		print ord(resp[0])
		RS232_1.write(resp)
	
	resp2 = RS232_1.read(1)
        resp2_l = len(resp2)
	print (str(datetime.now()) + ' - dane2 = ' + str(resp2_l))
		
	if len(resp2)>0:
		print ord(resp2[0])
		RS232_0.write(resp)


			
	counter += 1

	if counter >= 1000:
		print('----------------------------------------------------')
		print(datetime.now())
		print('----------------------------------------------------')
		counter = 0

		


