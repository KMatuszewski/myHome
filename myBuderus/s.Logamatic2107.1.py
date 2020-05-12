import serial
import time
from datetime import datetime

s = serial.Serial(           
               port='/dev/ttyUSB0',
               baudrate = 2400,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1)

post=False
print (s.name )

#0xEE 0x00 0x00 0x10 0x03 0xFD
s.flushInput ()
s.flushOutput ()
s.write (b"\x02")
now=datetime.now()
print(now.strftime("%d %H:%M:%S.%f") + " --> STX")

message=[]

try:
  while True:
    time.sleep(0.1)
    time.sleep(0.1)
    time.sleep(0.1)
    time.sleep(0.1)
    if s.inWaiting ():
        now=datetime.now()
        #print (now.strftime("%d %H:%M:%S.%f") + "   <-X- %3.2X"% s.inWaiting (),)
        while s.in_waiting:
          char= s.read ()
          message.append("%2.2X"% ord(char))
        print (now.strftime("%d %H:%M:%S.%f") + " <-- Mess ",message)
        
        if len (char):
            #print (now.strftime("%d %H:%M:%S.%f") + " <--- %2.2X"% ord (char),)
            if ord (char)== 0x10:
                #s.write (b"\xEE\x00\x00\x10\x03\xFD")
                post=True
            elif ord (char)== 0x02:
                if post:
                    
                    #s.write (b"\x10")
                    #print (now.strftime("%d %H:%M:%S.%f") + " --> DLE")
                    a=1
            elif not post:
                
                #s.write (b"\x02")
                #print (now.strftime("%d %H:%M:%S.%f") + " --> STX")
                a=2
        if len(message) == 1:
          if message[0] == '02':
            s.write (b"\x10")
            print (now.strftime("%d %H:%M:%S.%f") + " --> DLE2")
        if len(message) >=2:
          s.write (b"\x10")
          now=datetime.now()
          print (now.strftime("%d %H:%M:%S.%f") + " --> DLE3")
        message.clear()

except KeyboardInterrupt as e:
  logging.info("Stopping...")
