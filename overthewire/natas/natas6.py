#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas6.py
  es

Level 6 → Level 7
Username: natas6
URL:      http://natas6.natas.labs.overthewire.org
password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
problem:Input secret: View sourcecode

write up:
  1.  in the sorce code we find a line: include "includes/secret.inc";
  2.  Open   http://natas6.natas.labs.overthewire.org/includes/secret.inc
        output: <?
        $secret = "FOEIUWGHFEEUHOFUOIU";
           ?>
  3. in input box of first page put "FOEIUWGHFEEUHOFUOIU"
     Output:
	     Access granted. The password for natas7 is

 
'''
import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'


url = 'http://%s.natas.labs.overthewire.org/' % username


response = requests.get(url, auth = (username, password) )


print('\nURL = ',url,'\n')

content = response.text
print("1. response.text \n\n",response.text)



#results =re.findall(' natas7 is (.*)</div>', content)[0]
#print (results)
 