import os
import json
import re
import fileinput
import sys
import time
from pprint import pprint
from collections import Counter

Path = "./data/"
filelist = os.listdir(Path)

n = 497
i = 0

while i <= n:
	aj  = ''.join(str(i) for i in ("./data/memo",'{0:04}'.format(i),".txt"))
	bj = ''.join(str(i) for i in ("./data/cbdate",'{0:04}'.format(i),".txt"))
	print(aj, bj)
#aj = ('./data/memo0002.txt')
#bj = ('./data/cbdate0002.txt')
	with open(bj,'r') as b_json, open(aj,'r') as a_json:
		while True:
			try:
				bdata = json.load(b_json)
				buri = (bdata['uri'])
				bdate = (bdata['estimated-creation-date'])
			except ValueError:
				print('No CarbonDate',bj)
			try:	
				adata = json.load(a_json)
				auri = (adata['original_uri'])
				alist = (len(adata['mementos']['list']))
				print('memo',auri,' carb ', buri)
				if auri == buri and type(auri) is type(buri):
					print('MEMO Website: ', auri,' CarbonDate Website: ', buri,' Carbondate est date is ', bdate)
					print(bdate,',',alist,file=open('b_date_memto.csv','a'))
					i += 1
			except ValueError:
				print('No Memo',aj,"    ",bj)
				print('No MEMO Website, but CarbonDate Website:', buri, 'estimate date is ',bdate,file=open('b_date_no_memto.txt','a'))
				i += 1
			break		
	a_json.close
	b_json.close

i += 1

