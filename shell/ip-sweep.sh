#!/bin/bash

addr = 10.0.2.15
or ip in `seq 1 254`; do
    ping -c 1 $addr.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
  done
