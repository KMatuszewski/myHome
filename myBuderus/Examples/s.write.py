import time
import serial
from datetime import datetime

RS232 = serial.Serial(
	port='/dev/ttyUSB0',
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



while 1:
	RS232.write('A'.encode('utf-8'))
	RS232.write('B'.encode('utf-8'))

	time.sleep(10)
	now=datetime.now()
	dt_string=now.strftime("%Y.%m.%d %H:%M:%S")
	print(dt_string + ' - ' + str(counter) + ' = ')
	counter += 1


