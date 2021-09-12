#!/usr/bin/env python3
'''
request-http.py
https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
'''
import requests
import re

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % username
cookies = { "loggedin" : "1" }

reponse = requests.get(url, auth = (username, password))
session = requests.Session()


response_session = session.get(url, auth = (username, password), cookies = cookies )
print("1.response_session.cookies \n",response_session.cookies)
print("2.response_session.text \n",response_session.text)
print("3.reponse\n\n",reponse)
print("=================")
print("4.reponse.text\n\n",reponse.text)
print("=================")
r = requests.head(url)
print("5,head\n\n",r)
print("=================")


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print("6.r.url\n\n",r.url)
print("=================")

print("7.r.status_code = ",r.status_code)
print("8. r.encoding = ",r.encoding )
print("9.r.json()  = ", r.json())
 




