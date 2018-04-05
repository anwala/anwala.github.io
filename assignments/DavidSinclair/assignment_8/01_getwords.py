#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import re
import math
import os, os.path

path ='/home/david/Documents/cs532/assignment8_draft/train/'

for file in os.listdir(path):
     if file.endswith(".txt"):
          print(file,file=open('01names.txt','a'))
with open('01names.txt') as f:
    text = f.read().splitlines()
for name in text:
    filename=path+name             
    with open(filename) as f:
         doc = f.read()
         print(doc)
         splitter=re.compile('\\W*')
         # Split the words by non-alpha characters
         #words=[s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
         words=[s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
         # Return the unique set of words only
         print(words,file=open('01words.txt','a'))
#toreturn = dict([(w,1) for w in words])
#print(toreturn)
