#!/usr/bin/env python
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas0.py
https://www.youtube.com/watch?v=CT7ujrwtnsM&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V
'''
import requests
import re

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org' % username
print(url)
reponse = requests.get(url, auth = (username, password))
content = reponse.text
print(reponse )
print (content)
pass_list = re.findall('<!--The password for natas1 is (.*) -->', content)
#Regular  expersion all strings after '<!....natas1 is'
print (pass_list[0])