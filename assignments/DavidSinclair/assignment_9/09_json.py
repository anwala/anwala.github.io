import os
import json
import re
import fileinput
import sys
import time
from pprint import pprint
from collections import Counter

Path = "./data1/"
filelist = os.listdir(Path)

for i in filelist:
	if i.startswith("memo0") and i.endswith(".txt"):
		with open(Path + i, 'r') as infile:
			filename = Path + i
			searchlines = infile.readlines()
		for i, line in enumerate(searchlines):
			if "404 page not found" in line:
				print('This is a 404 file ', filename ,file=open('memento_404.txt','a'))
				print('This is a 404 file ', filename)
			else:
				print(filename, file=open('memento.txt','a'))
				print(filename)

#Takes all the 200 code links and makes sure there are no duplicates
content = open('memento.txt', 'r').readlines()
content_set = set(content)
cleandata = open('memento.file', 'w')

for line in content_set:
	cleandata.write(line)

#with open('memento.json') as json_file:
#	print(json_file)

with open('memento.file','r') as file_list:
	filename = file_list.read().splitlines()
#	print(filename)
#	print(len(filename))
	for idx,filename in enumerate(filename):
#		print(idx,'\n')
#		print(filename,'\n')
		with open(filename, 'r') as json_file:
			try:	
				json_data = json.load(json_file)
				print(len(json_data['mementos']['list']),file=open('histograph1.data','a'))
				print(filename, ",",len(json_data['mementos']['list']),file=open('histograph1.data.csv','a'))	
			except ValueError:
				print("JSON object issue: ",filename, file=open('memojson_fail.txt', 'a'))

#	print('This is below text=f.read ',text)
#	for idx,line in enumerate(text):
#		print('this is below for idx',line)
#		with open(line) as data:
#			print('This if with open ',data)
#			json_data = json.load(json_file)
#			print(len(json_data['mementos']['list']))	
#	for p in json_data:
#
#		print(p.count(['mementos']['list']0))
#		print(Counter(json_data['mementos']['list']))
#		print(len(json_data['mementos']['list']))
#
