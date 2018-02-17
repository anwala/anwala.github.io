import os, os.path
import re
import re
from collections import Counter


# path joining version for other paths
DIR = '/home/david/Documents/cs532/assignment3_draft/large/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

for file in os.listdir(DIR):
	if file.endswith(".txt"):
#		print(os.path.join(DIR, file))
		print(file,file=open('txtname7.txt','a'))
	
with open('txtname7.txt') as f:
    text = f.read().splitlines()
for name in text:
	filename=DIR+name
	print(filename)
	with open(filename) as fi:
		fitext = fi.read().splitlines()
		print(fitext,file=open('quest7.txt','a'))

