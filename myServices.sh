#!/bin/sh
#To jest komentarz.

echo "My Services - /lib/systemd/system/"
echo "---------------------------------------------------------------"
echo "logamatic2107.service"
echo "logamatic2107m.service"
echo "shelly.service"
echo "m.Raspberry.service"
echo "---------------------------------------------------------------"
sudo systemctl list-unit-files | grep enabled
echo "---------------------------------------------------------------"
sudo systemctl status logamatic2107.service 
echo "---------------------------------------------------------------"
sudo systemctl status logamatic2107m.service 
echo "---------------------------------------------------------------"
sudo systemctl status shelly.service 
echo "---------------------------------------------------------------"
sudo systemctl status m.Raspberry.service 
echo "---------------------------------------------------------------"


