#!/usr/bin/env python3
'''
Level 15 → Level 16
BLIND SQL Injection
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas15.py
www.youtube.com/watch?v=14eE7LSHlKc&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=13
Understanding Blind SQL Injection
https://www.youtube.com/watch?v=vz3XVCPBSbA

Username: natas15
URL:      http://natas15.natas.labs.overthewire.org
password:   AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
problem:

write up:



Manual Mode
https://www.jonyschats.nl/writeups/overthewire/natas/natas15/

'''


import requests

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username


session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print (content)


