#!/bin/sh
cat /home/pi/airly/output.txt | mail -s "Pomiary zanieczyszczeń powietrza" km.matuszewski@gmail.com
#cat /home/pi/airly/output.txt | mail -s "Pomiary zanieczyszczeń powietrza" tomasz.bialik@wp.pl

