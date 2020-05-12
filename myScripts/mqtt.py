#!/usr/bin/python3

import time
import os
from datetime import datetime
import paho.mqtt.client as mqtt

NOP = 0
T_AusTemp = " 0"
T_Ein = " 0"
T_Aus = " 0"
T_Kessel = " 0"
T_Test = " 0"
P_8000 = " 0"
P_8001 = " 0"
P_8002 = " 0"
P_8003 = " 0"
P_8004 = " 0"
P_8008 = " 0"
P_8112 = " 0"
P_8113 = " 0"
P_8114 = " 0"
P_8115 = " 0"
P_8116 = " 0"
P_8425 = " 0"
P_8426 = " 1"
P_8427 = " 0"
P_8429 = " 0"
P_882A = " 0"
P_8830 = " 0"
P_8831 = " 0"
P_8832 = " 0"
P_8833 = " 0"
P_8834 = " 0"
P_8835 = " 0"
P_8836 = " 0"
P_8837 = " 0"
P_8838 = " 0"
P_8839 = " 0"
P_883A = " 0"
P_883B = " 0"
P_893D = " 0"

sMQTT_Message = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + "Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/MQTTpublisher")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload))
    global sMQTT_Message
    if msg.topic == "/MQTTpublisher/Logamatic2107":
        sMQTT_Message = str(msg.payload.decode("utf-8"))
    else:
        sMQTT_Message = "?"
    
    
def on_log(client, obj, level, string):
    #print(now.strftime("%H:%M:%S.%f") + " --> " + string)
    fileName = "/home/pi/buderus/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()





def DataRead():
    fileName = "/home/pi/myHome/myScripts/Buderus_144.txt"
    file = open(fileName,"r")  
    for sLine in file:
        nr = sLine[2:5]
        if nr == "144":
            global T_AusTemp
            T_AusTemp = sLine[7:15].strip()
        elif nr == "145":
            global P_8000
            P_8000 = sLine[7:15].strip()
        elif nr == "146":
            global P_8003
            P_8003 = sLine[7:15].strip()
        elif nr == "147":
            global P_882A
            P_882A = sLine[7:15].strip()
        elif nr == "148":
            global P_8004
            P_8004 = sLine[7:15].strip()
        elif nr == "149":
            global P_8008
            P_8008 = sLine[7:15].strip()
        elif nr == "150":
            global P_8427
            P_8427 = sLine[7:15].strip()
        elif nr == "151":
            global P_8426
            P_8426 = sLine[7:15].strip()
        elif nr == "152":
            global P_8429
            P_8429 = sLine[7:15].strip()
        elif nr == "153":
            global P_8425
            P_8425 = sLine[7:15].strip()
        elif nr == "154":
            xxxx = sLine[7:15].strip()
        elif nr == "155":
            global P_8836
            P_8836 = sLine[7:15].strip()
        elif nr == "156":
            global P_8837
            P_8837 = sLine[7:15].strip()
        elif nr == "157":
            global P_8838
            P_8838 = sLine[7:15].strip()
        elif nr == "158":
            global T_Aus
            T_Aus = sLine[7:15].strip()
        elif nr == "159":
            global T_Ein
            T_Ein = sLine[7:15].strip()    
        else:
            NOP=0
            #print (sLine[2:5] + ' = ' + sLine[7:20].strip())
    file.close()

    fileName = "/home/pi/myHome/myScripts/Buderus_160.txt"
    file = open(fileName,"r")
    for sLine in file:
        nr = sLine[2:5]
        if nr == "162":
            global P_8832
            P_8832 = sLine[7:15].strip()
        elif nr == "163":
            global T_Kessel
            T_Kessel = sLine[7:15].strip()
        elif nr == "170":
            global P_893D
            P_893D = sLine[7:15].strip()
        elif nr == "171":
            global P_8001
            P_8001 = sLine[7:15].strip()
        else:
            NOP=0
            #print (sLine[2:5] + ' = ' + sLine[7:15].strip())  
    file.close()
    
    global T_Test 
    T_Test = "99"


def MQTTSend():
    global NOP
    global T_AusTemp
    global T_Ein
    global T_Aus
    global T_Kessel
    global T_Test
    global P_8000
    global P_8001
    global P_8002
    global P_8003
    global P_8004
    global P_8008
    global P_8112
    global P_8113
    global P_8114
    global P_8115
    global P_8116
    global P_8425
    global P_8426
    global P_8427
    global P_8429
    global P_882A
    global P_8830
    global P_8831
    global P_8832
    global P_8833
    global P_8834
    global P_8835
    global P_8836
    global P_8837
    global P_8838
    global P_8839
    global P_883A
    global P_883B
    global P_893D


    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mxHHMM -m " + sHHMM
    os.system(bashCommand)
    
    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mxHHMMSS -m " + sHHMMSS
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx893C -m " + T_AusTemp + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx80001 -m " + P_8000 + "/" + P_8001.strip()
    os.system(bashCommand)

    # 1 - HK_Betriebswerte2   [ "-", "Sommer", "Tag", "Keine Kommunikation mit FB", "FB fehlerhaft", "Fehler Vorlauffuehler", "Maximaler Vorlauf","Externer Stoehreingang", "Frei" ],
    P_8000 = P_8000.strip()
    P_8001 = P_8001.strip()

    S_8001 = ""
    if int(P_8001) & 1:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8001_Sommer -m Lato"
        os.system(bashCommand)
    else:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8001_Sommer -m Zima"
        os.system(bashCommand)

    #Tag/Night
    if int(P_8001) & 2:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8001_Tag -m Dzień"
        os.system(bashCommand)
    else:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8001_Tag -m Noc"
        os.system(bashCommand)


    S_8000 = ""
    if int(P_8000) & 4:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8000_AM -m Auto"
        os.system(bashCommand)
    elif int(P_8000) & 128:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8000_AM -m Man"
        os.system(bashCommand)
    else:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8000_AM -m ???"
        os.system(bashCommand)

    #Warmwasservorrang
    #---------------------------------------------------
    if int(P_8000) & 8:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8000_WW -m CW_ON"
        os.system(bashCommand)
    else:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8000_WW -m CW_OK"
        os.system(bashCommand)


    #bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8001s -m " + S_8001
    #os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8002 -m " + P_8002 + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8003 -m " + P_8003 + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8004 -m " + P_8004 + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8008 -m " + P_8008 + "%"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx882B -m " + T_Kessel + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx882C -m " + T_Aus + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx882D -m " + T_Ein + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx882CD -m " + T_Ein + "/" + T_Aus + "°C"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx84267 -m " + P_8427 + "/" + P_8426 + "°C"
    os.system(bashCommand)


    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8832 -m " + P_8832
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx893Cn -m " + T_AusTemp
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx893Dn -m " + P_893D
    os.system(bashCommand)


    #	WW_Pumpentyp = [‐,Ladepumpe,Zirkulationspumpe,Absenkung Solar,Frei,Frei,Frei,Frei,Frei]
    #	0x8429: 'Ladepumpe'                       ['aus', 'Ladepumpe', 'Warmwasserpumpe', 'beide']
    P_8429 = P_8429.strip()
    if P_8429 == "0":
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8429 -m " + "OFF"
    elif P_8429 == "1":
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8429 -m " + "Uzupeł"
    elif P_8429 == "2":
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8429 -m " + "Cyrkul"
    elif P_8429 == "3":
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8429 -m " + "Solar"
    else:
        bashCommand = "mosquitto_pub -h broker.hivemq.com -t /MQTTpublisher/mx8429 -m " + "??"
    os.system(bashCommand)
    
    
    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /kmPI/Logamatic2107/mx882B -m " + T_Kessel + "°C"
    bashCommand = bashCommand + " -u km -P kmPImqtt"
    os.system(bashCommand)

    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /kmPI/Logamatic2107/mx882CD -m " + T_Ein + "/" + T_Aus + "°C"
    bashCommand = bashCommand + " -u km -P kmPImqtt"
    os.system(bashCommand)


    bashCommand = "mosquitto_pub -h broker.hivemq.com -t /kmPI/Logamatic2107/mx893Cn -m " + T_AusTemp
    bashCommand = bashCommand + " -u km -P kmPImqtt"
    os.system(bashCommand)



now = datetime.now()

# This is the Publisher
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Uncomment to enable debug messages
client.on_log = on_log
client.connect("broker.hivemq.com",1883,60)
#client.subscribe("/kmPI/Raspberry")
client.publish("/MQTTpublisher/MQTT_Test", "Start - " + now.strftime("%H:%M:%S"));




DataRead()
sHHMM = time.strftime("%H:%M")
sHHMMSS = time.strftime("%H:%M:%S")

print(now.strftime("%Y.%m.%d %H:%M:%S.%f"))

MQTTSend()

now = datetime.now()
print(now.strftime("%Y.%m.%d %H:%M:%S.%f"))

time.sleep(1)
time.sleep(5)
time.sleep(5)
DataRead()
time.sleep(1)
sHHMMSS = time.strftime("%H:%M:%S")
MQTTSend()

now = datetime.now()
print(now.strftime("%Y.%m.%d %H:%M:%S.%f"))

time.sleep(1)
time.sleep(5)
time.sleep(5)
DataRead()
time.sleep(1)
sHHMMSS = time.strftime("%H:%M:%S")
MQTTSend()

now = datetime.now()
print(now.strftime("%Y.%m.%d %H:%M:%S.%f"))
