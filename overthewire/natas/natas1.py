#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas1.py
https://www.youtube.com/watch?v=CT7ujrwtnsM&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V
https://docs.python-requests.org/en/master/

Level 1 → Level 2
Username: natas1
URL:      http://natas1.natas.labs.overthewire.org
password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
problem:  You can find the password for the next level on this page,
 but right clicking has been blocked! 

'''
import requests
import re

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % username

reponse = requests.get(url, auth = (username, password))
content = reponse.text

# print content
reply = re.findall('<!--The password for natas2 is (.*) -->', content)[0]
print (reply)
