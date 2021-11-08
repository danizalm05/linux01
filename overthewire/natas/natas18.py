#!/usr/bin/env python3
'''
3:37
Level 18 → Level 19
TIMING ATTACK SQL Injection

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas18.py

https://www.youtube.com/watch?v=C9yxUTQLbRI&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=16
https://www.youtube.com/watch?v=vz3XVCPBSbA

Username: natas18
URL:      http://natas18.natas.labs.overthewire.org
username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
problem:

write up:



Manual Mode


'''
import string

import requests
import re
from string import *

from time import *

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(characters)

from pyodbc import lowercase

username = 'natas18'
username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text

print (content)
