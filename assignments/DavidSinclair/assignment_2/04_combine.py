import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate


#Takes the validated url and attempts to get a server code of 200
with open('200.txt') as f:
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
	print(url)	
	print(url, file=open("200comp.txt", "a"))

with open('300good.txt') as f:
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
	print(url)
	print(url, file=open("200comp.txt", "a"))

