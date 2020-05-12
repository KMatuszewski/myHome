#!/usr/bin/python3

import urllib.request, json
import requests


url = "http://192.168.5.101/status"

try:
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    data = json.loads(r.decode('utf-8'))


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


    print(myShellyTime)
    print(myShellyIP)
    print(myShellyON)
    print(t1,t2,p1,p2)
    print(pc1,pc2,pc3)


except:
  print("An exception occurred")

