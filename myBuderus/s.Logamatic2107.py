#!/usr/bin/python3

import serial
import time
from datetime import datetime
import paho.mqtt.client as mqtt
from Logamatic2107 import MessageDecoding, DataRead, DataWrite, DataGet


sMQTT_Message = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + "Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/MQTTpublisher/Logamatic2107")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload))
    global sMQTT_Message
    if msg.topic == "/MQTTpublisher/Logamatic2107":
        sMQTT_Message = str(msg.payload.decode("utf-8"))
    else:
        sMQTT_Message = "?"
    fileName = "/home/pi/myHome/myLogs/MQTT_" + now.strftime("%Y%m%d") + ".txt"
    file = open(fileName,"a")
    #file.write('\n')
    file.write('----------------------------------------------------\n')
    file.write(now.strftime("%Y.%m.%d %H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload.decode("utf-8")) + '\n')
    #file.write('----------------------------------------------------\n')
    file.close()
    


def on_log(client, obj, level, string):
    #print(now.strftime("%H:%M:%S.%f") + " --> " + string)
    fileName = "/home/pi/myHome/myLogs/MQTT_" + now.strftime("%Y%m%d") + ".txt"
    file = open(fileName,"a")
    #file.write('\n')
    file.write('----------------------------------------------------\n')
    file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    #file.write('----------------------------------------------------\n')
    file.close()


def write_log(string):
    now=datetime.now()
    fileName = "/home/pi/myHome/myLogs/Buderus_" + now.strftime("%Y%m%d") + ".txt"
    file = open(fileName,"a")
    file.write('\n')
    file.write('----------------------------------------------------\n')
    file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    file.write('----------------------------------------------------\n')
    file.close()



print('---Czekamy-------')
for x in range(3):
  time.sleep(1)
  #print('-',end="")
print('')
print('---Start  -------')


s = serial.Serial(port = '/dev/ttyUSB0',
                  baudrate = 2400)
                  #timeout=5.0)

post=False
print (s.name )

message=[]

print('----------------------------------------------------')
print(datetime.now())
print(s.name)
if s.isOpen():
	print('Port ' + s.name + ' is open ...')
else:
	print('Port ' + s.name + ' is closed ...')
print('----------------------------------------------------')

now=datetime.now()
fileName = "/home/pi/myHome/myLogs/Buderus_" + now.strftime("%Y%m%d") + ".txt"
file = open(fileName,"a")
file.write('\n')
file.write('--------------------------------------------------------------------------------------\n')
file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '  Start new session' + '\n')
file.write('--------------------------------------------------------------------------------------\n')
file.write('\n')
file.write('----------------------------------------------------\n')
file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '\n')
file.write(s.name + '\n')
if s.isOpen():
	file.write('Port ' + s.name + ' is open ...\n')
else:
	file.write('Port ' + s.name + ' is closed ...\n')
file.write('----------------------------------------------------\n')
file.close()

# This is the Publisher

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Uncomment to enable debug messages
client.on_log = on_log
client.connect("broker.hivemq.com",1883,60)
#client.subscribe("/MQTTpublisher/Logamatic2107")
client.publish("/MQTTpublisher/Logamatic2107", "Start");
client.publish("/MQTTpublisher/Logamatic2107_ACK", "");



DataRead()

timestamp=False;
#0xEE 0x00 0x00 0x10 0x03 0xFD
s.flushInput ()
s.flushOutput ()
now=datetime.now()
s.write (b"\x02")
#s.write (b"\x10")
print(now.strftime("%H:%M:%S.%f") + " --> STX")
a = 10

LogMode = True
LogModeStart = False

rc = 0;

try:
  while True:

    time.sleep(0.4)

    rc = client.loop()
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + str(rc))
    if rc != 0:
        client.reconnect()

    if ((sMQTT_Message != "") and (sMQTT_Message != "") and (sMQTT_Message[0] != "-")):
        client.publish("/MQTTpublisher/Logamatic2107_ACK", "" + sMQTT_Message);
        #sMQTT_Message = ""


    now=datetime.now()
    if (now.minute==0) or (now.minute==10) or (now.minute==20) or (now.minute==30) or (now.minute==40) or (now.minute==50):
        if (not timestamp):
            fileName = "/home/pi/myHome/myLogs/Buderus_" + now.strftime("%Y%m%d") + ".txt"
            file = open(fileName,"a")
            file.write('\n')
            file.write('----------------------------------------------------\n')
            file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '\n')
            file.write('----------------------------------------------------\n')
            file.close()
            timestamp = True
    else:
        timestamp = False

    if (now.hour==5) and (now.minute==0) and ((now.second==0) or (now.second==1) or (now.second==2)) and not LogModeStart:
        fileName = "/home/pi/myHome/myLogs/Buderus_" + now.strftime("%Y%m%d") + ".txt"
        file = open(fileName,"a")
        file.write('\n')
        file.write('----------------------------------------------------\n')
        file.write(now.strftime("%Y.%m.%d %H:%M:%S") + ' Log Mode ON    \n')
        file.write('----------------------------------------------------\n')
        file.close()
        LogMode = True
        LogModeStart = True
        s.flushInput ()
        s.flushOutput ()
        s.write (b"\x02")
        #s.write (b"\x10")
        print(now.strftime("%H:%M:%S.%f") + " --> STX")
        time.sleep(0.4)


    if (now.hour==5) and (now.minute==0) and (now.second>2) and LogModeStart:
        LogModeStart = False

    

    if s.inWaiting ():
        
        now=datetime.now()
        #print (now.strftime("%H:%M:%S.%f") + "   <-X- %3.2X"% s.inWaiting (),)
        while s.in_waiting:
          char= s.read ()
          message.append("%2.2X"% ord(char))
        print (now.strftime("%H:%M:%S.%f") + " <-- Mess ",message)

        if ((len(message) == 1) and LogMode):
          if message[0] == '10':
            s.write (b"\xEE\x00\x00\x10\x03\xFD")
            print (now.strftime("%H:%M:%S.%f") + " --> Kommando EE 00 00 10 03 FD")
            LogMode = False
          if message[0] == '02':
            s.write (b"\x10")
            print (now.strftime("%H:%M:%S.%f") + " --> DLE1")
            LogMode = False
        
        if ((len(message) == 1) and not LogMode):
          if message[0] == '02':
            
            if sMQTT_Message == "D":
                a = 0x07 ^ 0x00
                a = a ^ 0x65
                a = a ^ 0x65
                a = a ^ 0x65
                a = a ^ 0x65
                a = a ^ 0x00
                a = a ^ 0x65
                a = a ^ 0x10
                a = a ^ 0x03
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x65\x01\x65\x10\x03\x70")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN = " + hex(a) )
                #print (hex(a))
                sMQTT_Message = ""
                write_log("DZIEN")
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "OK_D");

            elif sMQTT_Message == "N":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x65\x00\x65\x10\x03\x71")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN = " + hex(a) )
                sMQTT_Message = ""
                write_log("NOC")
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "OK_N");
            elif sMQTT_Message == "A":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x65\x02\x65\x10\x03\x73")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN = " + hex(a) )
                write_log("AUTO")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "OK_A");

            elif sMQTT_Message == "N14":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x1C\x65\x65\x65\x10\x03\x6D")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 14°C = " + hex(a) )
                write_log("N14")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N14");

            elif sMQTT_Message == "N15":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x1E\x65\x65\x65\x10\x03\x6F")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 15°C = " + hex(a) )
                write_log("N15")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N15");
            
            elif sMQTT_Message == "N16":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x20\x65\x65\x65\x10\x03\x51")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 16°C = " + hex(a) )
                write_log("N16")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N16");

            elif sMQTT_Message == "N17":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x22\x65\x65\x65\x10\x03\x53")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 17°C = " + hex(a) )
                write_log("N17")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N17");
          
            elif sMQTT_Message == "N18":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x24\x65\x65\x65\x10\x03\x55")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 18°C = " + hex(a) )
                write_log("N18")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N18");
           
            elif sMQTT_Message == "N19":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x26\x65\x65\x65\x10\x03\x57")
                print (now.strftime("%H:%M:%S.%f") + " --> NOC 19°C = " + hex(a) )
                write_log("N19")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "N19");

           
            elif sMQTT_Message == "D14":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x1C\x65\x65\x10\x03\x6D")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 14°C = " + hex(a) )
                write_log("D14")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D14");

            elif sMQTT_Message == "D15":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x1E\x65\x65\x10\x03\x6F")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 15°C = " + hex(a) )
                write_log("D15")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D15"); 

            elif sMQTT_Message == "D16":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x20\x65\x65\x10\x03\x51")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 16°C = " + hex(a) )
                write_log("D16")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D16");  

            elif sMQTT_Message == "D17":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x22\x65\x65\x10\x03\x53")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 17°C = " + hex(a) )
                write_log("D17")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D17");

            elif sMQTT_Message == "D18":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x24\x65\x65\x10\x03\x55")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 18°C = " + hex(a) )
                write_log("D18")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D18");

            elif sMQTT_Message == "D19":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x26\x65\x65\x10\x03\x57")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 19°C = " + hex(a) )
                write_log("D19")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D19");

            elif sMQTT_Message == "D20":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x28\x65\x65\x10\x03\x59")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 20°C = " + hex(a) )
                write_log("D20")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D20");

            elif sMQTT_Message == "D21":
                s.write (b"\x02")
                s.write (b"\x07\x00\x65\x65\x65\x30\x65\x65\x10\x03\x41")
                print (now.strftime("%H:%M:%S.%f") + " --> DZIEN 21°C = " + hex(a) )
                write_log("D21")
                sMQTT_Message = ""
                client.publish("/MQTTpublisher/Logamatic2107", "");
                client.publish("/MQTTpublisher/Logamatic2107_ACK", "D21");

            else:
                s.write (b"\x10")
                print (now.strftime("%H:%M:%S.%f") + " --> DLE2")


        if len(message) >=2:
          MessageDecoding(message)
          DataWrite()
          s.write (b"\x10")
          now=datetime.now()
          print (now.strftime("%H:%M:%S.%f") + " --> DLE3")
        message.clear()


except KeyboardInterrupt as e:
  logging.info("Stopping...")
  client.disconnect();



client.disconnect();
