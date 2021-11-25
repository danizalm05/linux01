#!/usr/bin/env python3
'''
3:37
Level 20 → Level 21


github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas20.py

https://www.youtube.com/watch?v=6UiRRF1mbaU&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=18


Username: natas19
URL:      http://natas19.natas.labs.overthewire.org
username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
problem:

write up:


'''
import string

import requests
#pip uninstall uuid pip install uuid
import re
from string import *

from time import *




username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text
print(content)