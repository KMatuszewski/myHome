import serial

s = serial.Serial(port = '/dev/ttyUSB0',
                  baudrate = 2400)
                  #timeout=5.0)

post=False
print (s.name )

#0xEE 0x00 0x00 0x10 0x03 0xFD
s.flushInput ()
s.flushOutput ()
s.write (b"\x02")
while True:
    if s.inWaiting ():
        char= s.read ()
        if len (char):
            print ("%3.2X"% ord (char))
            if ord (char)== 0x10:
                s.write (b"\xEE\x00\x00\x10\x03\xFD")
                post=True
            elif ord (char)== 0x02:
                if post:
                    s.write (b"\x10")
            elif not post:
                s.write (b"\x02")



