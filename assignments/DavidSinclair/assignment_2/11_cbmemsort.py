import operator  # Used tor sorting
from itertools import groupby
import os
import json
import re
import fileinput
import sys
import time
from pprint import pprint
from collections import Counter

Path = "./data/"
filelist = os.listdir(Path)

for i in filelist:
	if i.startswith("cbdate0") and i.endswith(".txt"):
		with open(Path + i, 'r') as infile:
			filename = Path + i
			searchlines = infile.readlines()
		for i, line in enumerate(searchlines):
			if "404 page not found" in line:
				print('This is a 404 file ', filename ,file=open('cbdfilename_404.txt','a'))
				print('This is a 404 file ', filename)
			else:
				print(filename, file=open('cbdfilename.txt','a'))
				print(filename)

#Takes all the duplicates away
content = open('cbdfilename.txt', 'r').readlines()
content_set = set(content)
cbdsort = sorted(content_set, key=str)
cleandata = open('cbdfilename.file', 'w')

for line in cbdsort:
        cleandata.write(line)


#Takes all the duplicates away from memo
contenta = open('memento.txt', 'r').readlines()
content_seta = set(contenta)
memosort = sorted(content_seta, key=str)
cleandataa = open('memento.file', 'w')

for line in memosort:
        cleandataa.write(line)

