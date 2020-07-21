import requests
import json

with open('test.raw') as f: #Smaller test file
    text = f.read().splitlines()

#text = 'http://memgator.cs.odu.edu/timemap/json/http://guardian.com'
#http://localhost:8888/#

for url in text:
	print('http://localhost:8888/cd/',sep='',*url,file=open("carbdate.txt", "a"))

with open('carbdate.txt') as f:
	text = f.read().splitlines()

print(text)
print(len(text))
'''
for url in text:
	r = requests.get(url)
	print('initial url',url)
	response = r.text
	print(response,file=open('./data/url0001','a'))
'''
for idx,url in enumerate(text):
	r = requests.get(url)
	response = r.text
	i = idx
	print('{0:04}'.format(i),url)
	print('{0:04}'.format(i),url,file=open('./data/cdkey.txt','a'))
	filename = ''.join(str(x) for x in ("./data/cbdate",'{0:04}'.format(i),".txt"))
	print(response,file=open(filename,'w'))
	
