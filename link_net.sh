#!/bin/sh
sudo chmod 777 /sys/bus/usb-serial/drivers/option1/new_id
echo 2c7c 6002 > /sys/bus/usb-serial/drivers/option1/new_id
echo -e "AT+QCFG=\"usbnet\",3\n\n" > /dev/ttyUSB1
echo -e "AT+QNETDEVCTL=1,1,1\n\n" > /dev/ttyUSB1
touch /home/pi/setup_net.txt
chmod 777 /home/pi/setup_net.txt
echo "done" >> /home/pi/setup_net.txt
