import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate


#Takes all the 200 code links and makes sure there are no duplicates
content = open('200comp.txt', 'r').readlines()
content_set = set(content)
cleandata = open('200clean.txt', 'w')

for line in content_set:
        cleandata.write(line)

