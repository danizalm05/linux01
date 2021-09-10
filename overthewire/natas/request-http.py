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

reponse = requests.get(url, auth = (username, password))
content = reponse.text

print("reponse\n\n",reponse)
print("=================")
print("content\n\n",content)
print("=================")
r = requests.head(url)
print("head\n\n",r)
print("=================")


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

print("r.url\n\n",r.url)
print("=================")

print("r.status_code = ",r.status_code)
print(" r.encoding = ",r.encoding )
print("r.json()  = ", r.json())
 




