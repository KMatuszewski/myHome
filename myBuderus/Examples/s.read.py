import time
import serial
from datetime import datetime


RS232 = serial.Serial(
	port='/dev/ttyUSB1',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

counter=0
print('----------------------------------------------------')
print(datetime.now())
print(RS232.name)
if RS232.isOpen():
	print('Port ' + RS232.name + ' is open ...')
else:
	print('Port ' + RS232.name + ' is closed ...')
print('----------------------------------------------------')
print(' ')


RS232.flushInput()
RS232.flushOutput()

while 1:
	resp = RS232.read(1)
        
	print ('Odczytane liczba danych = ' + str(len(resp)))
	print resp
	
	
	if len(resp)>0:
		print ord(resp[0])
		
				


	counter += 1


