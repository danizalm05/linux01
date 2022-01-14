#!/usr/bin/env python3
'''
Level 22 → Level 23
Cross-site Session Hijacking : Python Web Hacking
https://github.com/psmiraglia/ctf/blob/master/overthewire/natas/natas22.md
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas22.py
https://www.youtube.com/watch?v=NVuG0Pps-xk&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=20
Username: natas22
URL:      http://natas22.natas.labs.overthewire.org
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
problem:


write up:


'''
import requests
import re
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'


url0 = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url0, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)

