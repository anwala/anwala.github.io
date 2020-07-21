import csv
import operator
import re
import sys

sample = open("072movie.txt")
csv1 = csv.reader(sample, delimiter=' ')
sort = sorted(csv1, key=lambda x : (int(x[2]),int(x[1])))
with open("072movie.csv", 'wt') as f:
	writer = csv.writer(f)
	for eachline in sort:
		writer.writerow(eachline)
		print(eachline)
#,file=open('sortmovie.txt','a'))
