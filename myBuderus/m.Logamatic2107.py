#!/usr/bin/python3

import serial
import time
from datetime import datetime
import paho.mqtt.client as mqtt
from Logamatic2107 import MessageDecoding, DataRead, DataWrite


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
    fileName = "/home/pi/myHome/myLogs/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload.decode("utf-8")) + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()
    


def on_log(client, obj, level, string):
    #print(now.strftime("%H:%M:%S.%f") + " --> " + string)
    fileName = "/home/pi/myHome/myLogs/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()


def write_log(string):
    now=datetime.now()
    fileName = "/home/pi/myHome/myLogs/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
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


post=False

message=[]

print('----------------------------------------------------')
print(datetime.now())
print('----------------------------------------------------')

now=datetime.now()


# This is the Publisher
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Uncomment to enable debug messages
client.on_log = on_log
client.connect("broker.hivemq.com",1883,60)
#client.subscribe("/MQTTpublisher/Logamatic2107")
client.publish("/MQTTpublisher/Logamatic2107_Test", "Start");


# This is the Publisher
clientPI = mqtt.Client()
clientPI.on_connect = on_connect
clientPI.on_message = on_message
# Uncomment to enable debug messages
clientPI.on_log = on_log
clientPI.connect("broker.hivemq.com",1883,60)
#clientPI.subscribe("/kmPI/Raspberry")
clientPI.publish("/kmPI/Raspberry/A1_Test", "Start");


#DataRead()

timestamp=False;
now=datetime.now()


rc = 0;

try:
  while True:

    time.sleep(10)

    rc = client.loop()
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + str(rc))
    if rc != 0:
        client.reconnect()

    rc = clientPI.loop()
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + str(rc))
    if rc != 0:
        clientPI.reconnect()

    now=datetime.now()
    if (now.minute==0) or (now.minute==10) or (now.minute==20) or (now.minute==30) or (now.minute==40) or (now.minute==50):
        if (not timestamp):
            timestamp = True
    else:
        timestamp = False


        
    client.publish("/MQTTpublisher/Logamatic2107_Test", now.strftime("%M:%S"));
    clientPI.publish("/kmPI/Raspberry/A1_Test", now.strftime("%M:%S"));



except KeyboardInterrupt as e:
  logging.info("Stopping...")
  client.disconnect();
  clientPI.disconnect();



client.disconnect();
clientPI.disconnect();
