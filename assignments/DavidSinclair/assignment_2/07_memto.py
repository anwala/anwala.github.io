import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate

#Takes the urls from twitremove.txt and adds the memgator http to the front 
with open('twitremove.txt') as f:
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
       print('http://memgator.cs.odu.edu/timemap/json/',sep='',*url,file=open("memgat.txt", "a"))

with open('memgat.txt') as f:
       text = f.read().splitlines()

print(text)
print(len(text))

#Takes the memgator http information and puts it into a file in the data directory and creates a key to reference url to filename.
for idx,url in enumerate(text):
        r = requests.get(url)
        response = r.text
        i = idx
        print('{0:04}'.format(i),url)
        print('{0:04}'.format(i),url,file=open('./data/memokey.txt','a'))
        filename = ''.join(str(x) for x in ("./data/memo",'{0:04}'.format(i),".txt"))
        print(response,file=open(filename,'w'))

