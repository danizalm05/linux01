#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas2.py
https://www.youtube.com/watch?v=_u9Zb1TsUks&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=2  0:00
https://docs.python-requests.org/en/master/

Level 2 → Level 3
Username: natas3
URL:      http://natas1.natas.labs.overthewire.org
password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi 
problem:  There is nothing on this page 

Write up:
 1.  check the Source Code
   output:
        .... <img src="files/pixel.png">
		
 2. Opened the files directory:
       http://natas2.natas.labs.overthewire.org/files/ 
	output:
      Parent Directory	 	- 	 
           	pixel.png	2016-12-15 16:07 	303 	 
           	users.txt	2016-12-20 05:15 	145 	 	
 3.	 Open   'users.txt'
       output:
	    # username:password
			....
			charlie:G5vCxkVV3m
			natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14



'''
import requests
import re
 
username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

reponse = requests.get(url, auth = (username, password))
content = reponse.text

 
 
print (content)

 
reply = re.findall('natas3:(.*)', content)[0]
print (reply)
