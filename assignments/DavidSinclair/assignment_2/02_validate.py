import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate

#Gets the twt.py output and inputs into this python program
tests = [test.rstrip('\n') for test in open('twitter_links.raw')]
print("TEST DATA: ", tests)
print(len(tests))

#Validates if the links are valid and returns a response 
for test in tests:
    try:
        r = requests.head(test)
        print(r.status_code)
        if (r.status_code) >= 400:
                print(r.status_code, test, file=open("400ws.txt", "a",))
                print(test, file=open("400.txt", "a",))
        elif(r.status_code) >= 300 and (r.status_code) <= 399:
                print(r.status_code, test, file=open("300ws.txt", 'a'))
                print(test, file=open("300.txt", 'a'))
        elif(r.status_code) == 200:
                print(r.status_code, test, file=open("200ws.txt", 'a'))
                print(test, file=open("200.txt", 'a'))
        else:
                print(r.status_code, test, file=open("everythingelsews.txt", 'a'))
                print(test, file=open("everythingelse.txt", 'a'))
    except requests.ConnectionError:
        print("failed to connect",)
        print(test, file=open("notvalidurl.txt", "a",))
'''
#Takes the validated url and attempts to get a server code of 200
with open('validurl.txt') as f:
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
	response = requests.get(url)
	print('initial url',url)
	if response.history:
		print("Request was redirected")
		for resp in response.history:
			print(resp.status_code, ) 
			print(resp.url, file=open("300.txt", "a",))#copy redirect link to file.
			print("Final destination: ")
			print(response.status_code,)
			print(response.url, file=open("200.txt", "a"))#copy response url to file.
	else:
		print(url, file=open("200.txt", "a"))#copy url to file

#Takes all the 200 code links and makes sure there are no duplicates
content = open('200.txt', 'r').readlines()
content_set = set(content)
cleandata = open('200clean.txt', 'w')

for line in content_set:
        cleandata.write(line)


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


#Takes the urls from twitremove.txt and adds the carbondate http to the front
with open('twitremove.txt') as f: 
    text = f.read().splitlines()


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

file=open('200.txt', 'r')
urlcomp = file.read().split('\n')
file.close()

file=open('300.txt', 'r')
redirlink = file.read().split('\n')
file.close()

file=open('400.txt', 'r')
notfound = file.read().split('\n')
file.close()

file=open('200clean.txt', 'r')
cleantwitterurl = file.read().split('\n')
file.close()

file=open('twitter_links.raw', 'r')
twitterlinks = file.read().split('\n')
file.close()

file=open('notvalidurl.txt', 'r')
notvalid = file.read().split('\n')
file.close()

file=open('validurl.txt', 'r')
valid = file.read().split('\n')
file.close()

file=open('twitremove.txt', 'r')
twitremove = file.read().split('\n')
file.close()

file=open('twitonly.txt', 'r')
twitonly = file.read().split('\n')
file.close()

file=open('memgat.txt', 'r')
memgat = file.read().split('\n')
file.close()

file=open('carbdate.txt', 'r')
carbdate = file.read().split('\n')
file.close()


print(len(twitterlinks), "is the number of links from the orginal twitter search.")
print(len(notvalid), "is the number of links that were not valid.")
print(len(valid), "is the number of links that were valid.")
print(len(urlcomp), "is the number of urls with code 200")
print(len(redirlink), "is the number of urls with code 301")
print(len(notfound), "is the number of urls with code 400")
print(len(cleantwitterurl), "is the number of urls with out duplicates")
print(len(twitonly), "is the number of urls that had twitter.com")
print(len(twitremove), "is the number of urls with twitter.com removed")
print(len(memgat), "is the number of urls in memgat")
print(len(carbdate), "is the number of urls in carbdate")
'''
