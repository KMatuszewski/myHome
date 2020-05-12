#!/bin/bash

echo '--------------------------------------------------------------' > output.txt
date >> output.txt
echo '--------------------------------------------------------------' >> output.txt

pomiary=$(curl -X GET --header 'Accept: application/json' --header 'apikey: 5d966716c6e84f61840e50f1345a2bed' 'https://airapi.airly.eu/v1/nearestSensor/measurements?latitude=50.28&longitude=18.59&maxDistance=1000')

#pomiary2=$(echo $pomiary | python -m json.tool)
#echo $pomiary2 >> output.txt

#echo '------------' >> output.txt
#echo $pomiary  >> output.txt

#echo '-----------------------------------------------------------------' >> output.txt
#pm25=$(echo $pomiary2 | jq -r '.pm25')

meastime=$(echo $pomiary | python -c "import sys, json; print json.load(sys.stdin)['measurementTime']")
airQualityIndex=$(echo $pomiary | python -c "import sys, json; print json.load(sys.stdin)['airQualityIndex']")
pm10=$(echo $pomiary | python -c "import sys, json; print json.load(sys.stdin)['pm10']")
pm25=$(echo $pomiary | python -c "import sys, json; print json.load(sys.stdin)['pm25']")

echo "Czas Pomiaru = " "$meastime" >> output.txt
echo "AirQuality   = " "$airQualityIndex" >> output.txt
echo "Pomiar PM10  = " "$pm10" >> output.txt
echo "Pomiar PM25  = " "$pm25" >> output.txt

#echo ' ' >> output.txt
echo '--------------------------------------------------------------' >> output.txt

#echo `expr index "$pomiary2" "pm10"`
#echo $pomiary2 | jq -r '.pm10' >> output.txt
#echo '------------------------------' >> output.txt
#echo ${pomiarr2} | jq -r '.pm10' >> output.txt
#echo 'aaaaaaaaaaaaaa' >> output.txt
#echo $pomiary2 | python -c "import sys, json; print json.load(sys.stdin)['pm10']" >> output.txt


