import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate


#Takes the validated 200 codes that are not duplicates and removes the twitter.com urls.
err_occur = []
pattern = re.compile("twitter.com", re.IGNORECASE)
try:
        with open ('200clean.txt','rt') as in_file:
                for linenum, line in enumerate(in_file):
                        if pattern.search(line) != None:
                                err_occur.append((linenum, line.rstrip('\n')))
                        else:
                                print(line, file=open("twitline.txt",'a'))
                for iinenum, line in err_occur:
                        print(line, file=open("twitonly.txt",'a'))
except FileNotFoundError:
        print("Log file not found.")

#Removes blank lines from the twitline.txt and changes the name to twitremove.txt
for line in open('twitline.txt'):
  line = line.rstrip()
  if line != '':
    print(line, file=open('twitremove.txt','a'))

