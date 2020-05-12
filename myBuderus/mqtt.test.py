#!/usr/bin/python3

from __future__ import division
import serial
import time
from datetime import datetime
import paho.mqtt.client as mqtt
from Logamatic2107 import MessageDecoding, DataRead, DataWrite
from subprocess import PIPE, Popen
import psutil


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode()
    return float(output[output.index('=') + 1:output.rindex("'")])


def main():
    cpu_temperature = get_cpu_temperature()
    print('CpuTemp = {0:0.2f} C'.format(cpu_temperature))
    cpu_usage = psutil.cpu_percent(0.1, False)
    print('CpuUsage = {0:0.2f} %'.format(cpu_usage))
    print('CpuCount = {0:0.0f}'.format(psutil.cpu_count()))
    #freqs = psutil.cpu_freq()
    #print('CpuFreqCurrent = {0:0.2f} %'.format(freqs.current))
    #print('CpuFreqMin = {0:0.2f} %'.format(freqs.min))
    #print('CpuFreqMax = {0:0.2f} %'.format(freqs.max))

    ram = psutil.virtual_memory()
    ram_total = ram.total / 2**20       # MiB.
    print('RamTotal = {0:0.2f} MB'.format(ram_total))
    ram_used = ram.used / 2**20
    print('RamUsed = {0:0.2f} MB'.format(ram_used))
    ram_free = ram.free / 2**20
    print('RamFree = {0:0.2f} MB'.format(ram_free))
    ram_available = ram.available / 2**20
    print('RamAvailable = {0:0.2f} MB'.format(ram_available))
    ram_percent_used = ram.percent
    print('RamPercent = {0:0.2f} %'.format(ram_percent_used))

    print('FS = [')
    partition = psutil.disk_partitions()
    for part in partition:
        print('Mountpoint = ' + part.mountpoint)
        disk = psutil.disk_usage(part.mountpoint)
        disk_total = disk.total / 2**30     # GiB.
        print('DiskTotal = {0:0.2f} GB'.format(disk_total))
        disk_used = disk.used / 2**30
        print('DiskUsed = {0:0.2f} GB'.format(disk_used))
        disk_free = disk.free / 2**30
        print('DiskFree = {0:0.2f} GB'.format(disk_free))
        disk_percent_used = disk.percent
        print('DiskPercent = {0:0.2f} %'.format(disk_percent_used))
        print(',')
    print(']')









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
    fileName = "/home/pi/myHome/myBuderus/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S.%f") + " --> MQTT: " + msg.topic+" "+str(msg.payload.decode("utf-8")) + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()
    


def on_log(client, obj, level, string):
    #print(now.strftime("%H:%M:%S.%f") + " --> " + string)
    fileName = "/home/pi/myHome/myBuderus/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
    #file = open(fileName,"a")
    #file.write('\n')
    #file.write('----------------------------------------------------\n')
    #file.write(now.strftime("%Y.%m.%d %H:%M:%S") + " --> " + string + '\n')
    #file.write('----------------------------------------------------\n')
    #file.close()


def write_log(string):
    now=datetime.now()
    fileName = "/home/pi/myHome/myBuderus/MQTT2_" + now.strftime("%Y%m%d") + ".txt"
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
clientPI = mqtt.Client()
clientPI.on_connect = on_connect
clientPI.on_message = on_message
# Uncomment to enable debug messages
clientPI.on_log = on_log
clientPI.username_pw_set(username="maqfhzia",password="x7WzTFRNMD-Y")
clientPI.connect("farmer.cloudmqtt.com",12551,60)
#clientPI.subscribe("/kmPI/Raspberry")
clientPI.publish("/kmPI/Raspberry/A1_Test", "Start");


#DataRead()

timestamp=False;
now=datetime.now()


rc = 0;

try:
  while True:

    time.sleep(10)

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


    #main()    
    clientPI.publish("/kmPI/Raspberry/A1_Test", now.strftime("%M:%S"))
    clientPI.publish("/kmPI/Raspberry/CPU_Temp", get_cpu_temperature())
    
    disk = psutil.disk_usage("/")
    disk_free = disk.free / 2**30
    clientPI.publish("/kmPI/Raspberry/Disk_Free", '{0:0.2f} GB'.format(disk_free))
    disk_total = disk.total / 2**30     # GiB.
    clientPI.publish("/kmPI/Raspberry/Disk_Total", '{0:0.2f} GB'.format(disk_total))
    disk_used = disk.used / 2**30
    clientPI.publish("/kmPI/Raspberry/Disk_Used", '{0:0.2f} GB'.format(disk_used))
    disk_percent_used = disk.percent
    clientPI.publish("/kmPI/Raspberry/Disk_Percent", '{0:0.2f} %'.format(disk_percent_used))



    



except KeyboardInterrupt as e:
  logging.info("Stopping...")
  clientPI.disconnect();



clientPI.disconnect();
