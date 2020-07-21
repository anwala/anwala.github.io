import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate

#Takes the 300.txt file and and attempts to get a server code of 200
text = []

with open('300.txt') as f:
    text = f.read().splitlines()

print(text)
print(len(text))

for url in text:
	try:
		response = requests.get(url)
		print(response.history, response.url)
		for resp in response.history:
			print(response.history, response.url, resp.status_code, resp.url, file=open('300comp.txt','a'))
			
			if response.status_code == 200:
				print(response.status_code, response.url, 'save code 200')
				print(response.status_code, response.url, file=open('300goodws.txt','a'))
				print(response.url, file=open('300good.txt','a'))	
			else:
				print(response.status_code, response.url, 'save not')
				print(response.status_code, response.url, file=open('300failsws.txt','a'))
				print(response.url, file=open('300fails.txt','a'))

	except requests.ConnectionError:
		print("failed to connect",response.url)
		print(response.status_code, response.url, file=open('300connectfailws.txt','a'))
		print(response.url, file=open('300connectfail.txt','a'))

