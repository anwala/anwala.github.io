import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate


#Takes the urls from twitremove.txt and adds the carbondate http to the front
with open('twitremove.txt') as f: 
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
        print('http://localhost:8888/cd/',sep='',*url,file=open("carbdate.txt", "a"))

with open('carbdate.txt') as f:
        text = f.read().splitlines()

print(text)
print(len(text))

#Takes the carbondate http information and puts it into a file in the data directory and creates a key to reference url to filename.
for idx,url in enumerate(text):
        r = requests.get(url)
        response = r.text
        i = idx
        print('{0:04}'.format(i),url)
        print('{0:04}'.format(i),url,file=open('./data/cbdatekey.txt','a'))
        filename = ''.join(str(x) for x in ("./data/cbdate",'{0:04}'.format(i),".txt"))
        print(response,file=open(filename,'w'))

