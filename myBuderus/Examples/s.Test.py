import serial

s = serial.Serial(port = '/dev/ttyUSB0',
                  baudrate = 2400)
                  #timeout=1.0)

post=True
print (s.name )

#0xEE 0x00 0x00 0x10 0x03 0xFD
s.flushInput ()
s.flushOutput ()
s.write (b"\x10")
#print("------> STX")
while True:
    if s.inWaiting ():
        char= s.read ()
        if len (char):
            print ("<--- %3.2X"% ord (char),)
            if ord (char)== 0x10:
                #s.write (b"\xEE\x00\x00\x10\x03\xFD")
                s.write (b"\x10")
                print ("------> Kommando EE 00 00 10 03 FD")
                post=True
            elif ord (char)== 0x02:
                if post:
                    s.write (b'\x10')
                    print ("------> DLE")
            elif not post:
                #s.write (b"\x10")
                print ( "------> STX")