import csv
import math
import operator
import string
from collections import Counter
from math import sqrt
import re

#open('u.item', encoding = "ISO-8859-1")

with open('/home/david/Documents/cs532/assignment6_draft/ml-100k/u.item', encoding = "ISO-8859-1") as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		with open('072movie.csv') as mvs:
			for line2 in csv.reader(mvs, delimiter=","):
				if line2[2] == '1':
					if line2[1] == line[0]:	
						print(line2[2],'&',line[1],file=open('072movierank1.tsv','a'))	
				if line2[2] == '5':
					if line2[1] == line[0]:
						print(line2[2],'&',line[1],file=open('072movierank5.tsv','a'))
#with open("sortmovie.csv", 'wt') as f:
#writer = csv.writer(f)
#for eachline in sort:
#writer.writerow(eachline)

