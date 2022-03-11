#!/usr/bin/env python3
'''
Level 25 → Level 26
LFI to RCE with User-Agen
https://www.youtube.com/watch?v=K1rBD0lJ0o8&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=22

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas25.py

Username: natas25
URL:      http://natas25.natas.labs.overthewire.org
          http://natas25.natas.labs.overthewire.org/index-source.html
=======================================================


username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
problem:
write up:
'''
import requests
import re
username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'


url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
response = session.get(url, auth = (username, password) )

print("1. response.text \n------------------\n",response.text)
session = requests.Session()
