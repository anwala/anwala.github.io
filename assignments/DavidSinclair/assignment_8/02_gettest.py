#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import re
import math
import os, os.path

path ='/home/david/Documents/cs532/assignment8_draft/test/'

for file in os.listdir(path):
     if file.endswith(".txt"):
          print(file,file=open('02test.txt','a'))
