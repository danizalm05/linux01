#!/usr/bin/env python3
'''

https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas8.py
https://www.youtube.com/watch?v=6DrAoTiAFtA&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=6
https://docs.python-requests.org/en/master/


Level 8 → Level 9
Username: natas8
URL:      http://natas8.natas.labs.overthewire.org
password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
problem :  On successfully logging in the natas8 webpage, we will have a form in
           front of us.
           It says “Input secret:”
write up:
       In the source code and found that the secret is encoded.
	   Also, we have a function which encodes the secret.

	 $encodedSecret = "3d3d516343746d4d6d6c315669563362";
	 function encodeSecret($secret) {
             return bin2hex(strrev(base64_encode($secret)));
}

  So it looks like they tried to hide the secret by encoding the input in the
  following order:

a) base64_encode - Regular Base64 encoding
b) strrev - reverses a string
c) bin2hex - Convert binary data into hexadecimal representation
 We simply need to run the string
         3d3d516343746d4d6d6c315669563362
through the following proccess:

a) hex2bin
b) strrev
c) base64_decode

1. open  interactive php command line in   url:
        https://sandbox.onlinephpfunctions.com/
2.  Run the next 2 commands
     $encodedSecret = "3d3d516343746d4d6d6c315669563362";
     echo base64_decode(strrev(hex2bin($encodedSecret)));

 result: oubWYf2kBq
3. Input this string in the input box

output: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl



'''
import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'


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

print (re.findall('natas9 is (.*)', content)[0])
