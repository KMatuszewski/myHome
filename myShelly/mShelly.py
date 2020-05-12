#!/usr/bin/python3

import urllib.request, json
import mysql.connector
from mysql.connector import errorcode
import paho.mqtt.client as mqtt
import requests
import subprocess
import time
from datetime import datetime
from mysql.connector import Error

mS1 = False
mS2 = False
mS3 = False

sMQTT_Message = ""
sTempWewn = 0.0

def Shelly1(mydb,mycursor):
  url = "http://192.168.5.101/status"
  #print(url)
  try:
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req, timeout=5).read()
    data = json.loads(r.decode('utf-8'))

    #print(data)

    # extracting latitude, longitude and formatted address  
    # of the first matching location 
    myShellyMAC = data['mac']
    myShellyTime = data['time']
    myShellyIP = data['wifi_sta']['ip']
    myShellyON = data['relays'][0]['ison']
    myShellyUpTime = data['uptime']

    t1 = data['tmp']['tC'] 
    t2 = data['temperature']
    p1 = data['meters'][0]['total']
    p2 = data['meters'][0]['power']
    pc1 = data['meters'][0]['counters'][0]
    pc2 = data['meters'][0]['counters'][1]
    pc3 = data['meters'][0]['counters'][2]

    #print(myShellyTime)
    print(myShellyIP)
    #print(myShellyON)
    #print(t1,t2,p1,p2)
    #print(pc1,pc2,pc3)  
    mS1 = True    

  except:
    print("An exception occurred - Shelly 1")
    print('----------------------------------------------------')
    mS1 = False
    myShellyMAC = "00:00:00:00:00"
    t1 = 0
    p1 = 0
    p2 = 0
    myShellyUpTime = 0
    myShellyON = 0
    
  if (mS1):
    try:
      sql = "INSERT INTO myShelly (mac,temp,totalpower,power,uptime,relayON) VALUES (%s,%s,%s,%s,%s,%s)"
      val = (myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      mycursor.execute(sql,val)

      mydb.commit()
      #print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as e:
      print("An exception occurred - SQL1")
      print(sql)
      #print(val)
      print(myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      print('----------------------------------------------------')
      print("Error code:", e.errno)        # error number
      print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
      print("Error message:", e.msg)       # error message
      print("Error:", e)                   # errno, sqlstate, msg values
      s = str(e)
      print("Error:", s)
      print('----------------------------------------------------')
  else:
    print("No SQL INSERT - Shelly 1")
    print('----------------------------------------------------')

def Shelly2(mydb,mycursor):
  url = "http://192.168.5.102/status"

  try:
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req, timeout=5).read()
    data = json.loads(r.decode('utf-8'))

    # print data

    # extracting latitude, longitude and formatted address  
    # of the first matching location 
    myShellyMAC = data['mac']
    myShellyTime = data['time']
    myShellyIP = data['wifi_sta']['ip']
    myShellyON = data['relays'][0]['ison']
    myShellyUpTime = data['uptime']

    t1 = data['tmp']['tC'] 
    t2 = data['temperature']
    p1 = data['meters'][0]['total']
    p2 = data['meters'][0]['power']
    pc1 = data['meters'][0]['counters'][0]
    pc2 = data['meters'][0]['counters'][1]
    pc3 = data['meters'][0]['counters'][2]

    #print(myShellyTime)
    #print(myShellyIP)
    #print(myShellyON)
    #print(t1,t2,p1,p2)
    #print(pc1,pc2,pc3)
    mS2 = True

  except:
    print("An exception occurred - Shelly 2")
    print('----------------------------------------------------')
    mS2 = False
    myShellyMAC = "00:00:00:00:00"
    t1 = 0
    p1 = 0
    p2 = 0
    myShellyUpTime = 0
    myShellyON = 0

  if (mS2):
    try:
      sql = "INSERT INTO myShelly (mac,temp,totalpower,power,uptime,relayON) VALUES (%s,%s,%s,%s,%s,%s)"
      val = (myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      mycursor.execute(sql,val)

      mydb.commit()

      #print(mycursor.rowcount, "record inserted.")
    except mysql.connector.Error as e:
      print("An exception occurred - SQL2")
      print(sql)
      #print(val)
      print(myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      print('----------------------------------------------------')
      print("Error code:", e.errno)        # error number
      print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
      print("Error message:", e.msg)       # error message
      print("Error:", e)                   # errno, sqlstate, msg values
      s = str(e)
      print("Error:", s)
      print('----------------------------------------------------')
  else:
    print("No SQL INSERT - Shelly 2")
    print('----------------------------------------------------')

def Shelly3(mydb,mycursor):
  url = "http://192.168.5.103/status"

  try:
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req, timeout=5).read()
    data = json.loads(r.decode('utf-8'))

    # print data

    # extracting latitude, longitude and formatted address  
    # of the first matching location 
    myShellyMAC = data['mac']
    myShellyTime = data['time']
    myShellyIP = data['wifi_sta']['ip']
    myShellyON = data['relays'][0]['ison']
    myShellyUpTime = data['uptime']

    t1 = data['tmp']['tC'] 
    t2 = data['temperature']
    p1 = data['meters'][0]['total']
    p2 = data['meters'][0]['power']
    pc1 = data['meters'][0]['counters'][0]
    pc2 = data['meters'][0]['counters'][1]
    pc3 = data['meters'][0]['counters'][2]

    #print(myShellyTime)
    #print(myShellyIP)
    #print(myShellyON)
    #print(t1,t2,p1,p2)
    #print(pc1,pc2,pc3)
    mS2 = True

  except:
    print("An exception occurred - Shelly 3")
    print('----------------------------------------------------')
    mS2 = False
    myShellyMAC = "00:00:00:00:00"
    t1 = 0
    p1 = 0
    p2 = 0
    myShellyUpTime = 0
    myShellyON = 0

  if (mS2):
    try:
      sql = "INSERT INTO myShelly (mac,temp,totalpower,power,uptime,relayON) VALUES (%s,%s,%s,%s,%s,%s)"
      val = (myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      mycursor.execute(sql,val)

      mydb.commit()

      #print(mycursor.rowcount, "record inserted.")
    except mysql.connector.Error as e:
      print("An exception occurred - SQL3")
      print(sql)
      #print(val)
      print(myShellyMAC,t1,p1,p2,myShellyUpTime,myShellyON)
      print('----------------------------------------------------')
      print("Error code:", e.errno)        # error number
      print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
      print("Error message:", e.msg)       # error message
      print("Error:", e)                   # errno, sqlstate, msg values
      s = str(e)
      print("Error:", s)
      print('----------------------------------------------------')
  else:
    print("No SQL INSERT - Shelly 3")
    print('----------------------------------------------------')


def ShellyTH(mydb,mycursor):
  try:
    global sTempWewn
    url = 'https://shelly-4-eu.shelly.cloud/device/status'
    myobj = {'id': '58EE34', 'auth_key':'MTU0M2Z1aWQECD1F8EBD5D95FCDD3EA3FD255BF3FF18AE0E497C7C35C49504EF066F6C892D56B8121735BEC2BFE'}
                                         
    x = requests.post(url, data = myobj, timeout=5)

    #print(x.text)

    data = json.loads(x.text)
    #print (data)

    myShellyMAC = data['data']['device_status']['mac']
    myShellyHUM = data['data']['device_status']['hum']['value']
    myShellyTMP = data['data']['device_status']['tmp']['value']
    myShellyTCC = data['data']['device_status']['tmp']['tC']
    myShellySLE = data['data']['device_status']['_sleeping']
    myShellyBAT = data['data']['device_status']['bat']['voltage']
    myShellyBAV = data['data']['device_status']['bat']['value']
    myShellyUPD = data['data']['device_status']['_updated']
    myShellyTIM = data['data']['device_status']['uptime']
    myShellyUPT = data['data']['device_status']['uptime']

    sTempWewn = myShellyTMP
    #print (myShellyTMP)

    #print(myShellyMAC)
    #print(myShellyHUM)
    #print(myShellyTMP)
    #print(myShellyTCC)
    #print(myShellySLE)
    #print(myShellyBAT)
    #print(myShellyBAV)
    #print(myShellyUPD)
    #print(myShellyTIM)
    #print(myShellyUPT)
    mS3 = True
  except:
    print("An exception occurred - Shelly TH")
    print('----------------------------------------------------')
    mS3 = False
    myShellyMAC = "00:00:00:00:00"
    myShellyTMP = 0
    myShellyHUM = 0
    myShellyBAV = 0
    myShellyBAT = 0
    myShellyUPD = 0
    myShellySLE = 0
    myShellyTIM = 0
    myShellyUPT = 0

  if (mS3):
    try:
      sql = "INSERT INTO myShellyTH (mac,temp, hum, bat, bat_voltage,update_time, sleeping, device_time, uptime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (myShellyMAC,myShellyTMP,myShellyHUM,myShellyBAV,myShellyBAT,myShellyUPD,myShellySLE,myShellyTIM,myShellyUPT)
      #sql = "INSERT INTO myShellyTH (mac,temp, hum) VALUES (%s,%s,%s)"
      #val = (myShellyMAC,myShellyTMP,myShellyHUM)


      mycursor.execute(sql,val)

      mydb.commit()

      #print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as e:
      print("An exception occurred - SQL_TH")
      print(sql)
      #print(val)
      print(myShellyMAC,myShellyTMP,myShellyHUM,myShellyBAV,myShellyBAT,myShellyUPD,myShellySLE,myShellyTIM,myShellyUPT)
      print('----------------------------------------------------')
      print("Error code:", e.errno)        # error number
      print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
      print("Error message:", e.msg)       # error message
      print("Error:", e)                   # errno, sqlstate, msg values
      s = str(e)
      print("Error:", s) 
      print('----------------------------------------------------')
  else:
    print("No SQL INSERT - Shelly TH")
    print('----------------------------------------------------')

def SQLConnect():
  try:
    global mydb
    global mycursor
    mydb = mysql.connector.connect(
      host="mn14.webd.pl",
      user="van5656_Buderus",
      passwd="Baza911!",
      database="van5656_myHome"
    )
    mycursor = mydb.cursor()
    print('SQL Connection - ',mydb.is_connected())
    print('SQL Connection - ',mydb)
    print('----------------------------------------------------')
  except Error as e:
    print("Error while connecting to MySQL", e)
    print('----------------------------------------------------')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + "Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/MQTTpublisher/Shelly_CMD")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload))
    global sMQTT_Message
    if msg.topic == "/MQTTpublisher/Logamatic2107":
        sMQTT_Message = str(msg.payload.decode("utf-8"))
    else:
        sMQTT_Message = "?"
    fileName = "/home/pi/buderus/MQTT_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload.decode("utf-8")) + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()
    

def on_log(client, obj, level, string):
    #print(now.strftime("%H:%M:%S.%f") + " --> " + string)
    fileName = "/home/pi/buderus/MQTT_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()

def mqttSendData():
  try:
    now=datetime.now()
    rc = client.loop()
    print(now.strftime("%H:%M:%S.%f") + " --> MQTT: " + str(rc))
    if rc != 0:
        client.reconnect()
        rc = client.loop()
        print(now.strftime("%H:%M:%S.%f") + " --> MQTT: Reconnect" + str(rc))
        client.publish("/MQTTpublisher/Shelly", "ReConnect - " + now.strftime("%Y.%m.%d %H:%M:%S.%f"));

    client.publish("/MQTTpublisher/Shelly_TWewn", sTempWewn);
    client.publish("/MQTTpublisher/Shelly_HHMM", now.strftime("%Y.%m.%d %H:%M:%S.%f"));
    print("MQTT - OK - ", sTempWewn)
  except Error as e:
    mqttError = 1;
    print("MQTT - NOK - ", sTempWewn)
  print('----------------------------------------------------')

# --------------------------------------------------------------------
# Poczatek programu glownego
# --------------------------------------------------------------------

print('----------------------------------------------------')
print('Start - ', datetime.now())
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
client.publish("/MQTTpublisher/Shelly", "Start - " + now.strftime("%Y.%m.%d %H:%M:%S.%f"));
client.publish("/MQTTpublisher/Shelly_CMD", "Start");


try:
  mydb = mysql.connector.connect(
    host="mn14.webd.pl",
    user="van5656_Buderus",
    passwd="Baza911!",
    database="van5656_myHome"
  )
  mycursor = mydb.cursor()
except Error as e:
  print("Error while connecting to MySQL", e)
  print('----------------------------------------------------')

#SQL Connection Status
print('My SQL Connection - ',mydb.is_connected())
print('----------------------------------------------------')


timestamp=False;

try:
  while True:
    
    time.sleep(0.2)

    now=datetime.now()
    if (now.second==0):
      if (not timestamp):

        print("Poczatek : ", datetime.now())
        print('----------------------------------------------------')

        #SQL Connection Status
        print('My SQL Connection - ',mydb.is_connected())
        print('----------------------------------------------------')
        
        if (not mydb.is_connected()):
          SQLConnect()

        Shelly1(mydb,mycursor)
        print('Shelly 1 - ', datetime.now())
        print('----------------------------------------------------')

        if (not mydb.is_connected()):
          SQLConnect()

        Shelly2(mydb,mycursor)
        print('Shelly 2 - ', datetime.now())
        print('----------------------------------------------------')

        if (not mydb.is_connected()):
          SQLConnect()

        Shelly3(mydb,mycursor)
        print('Shelly 3 - ', datetime.now())
        print('----------------------------------------------------')

        if (not mydb.is_connected()):
          SQLConnect()
	
        ShellyTH(mydb,mycursor)
        print('Shelly TH - ', datetime.now())
        print('----------------------------------------------------')

        print("Koniec : ", datetime.now())
        print('----------------------------------------------------')

        mqttSendData()
        
        timestamp = True
        time.sleep(10)
        time.sleep(10)
        time.sleep(10)
        time.sleep(10)
        print("Koniec czekania : ", datetime.now())
        print('----------------------------------------------------')

        mqttSendData()

    else:
      timestamp = False
      #print('CCC')

    


except KeyboardInterrupt as e:
  logging.info("Stopping...")
