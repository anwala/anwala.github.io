import re
from datetime import datetime
import csv
import sys
from collections import defaultdict
import matplotlib.pyplot as plt

x=[]
y=[]

dates=[]
memos=[]

with open('b_date_memto.csv','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		date = row[0]
		dates.append(str.strip(date))
		memo = row[1]
		y.append(str.strip(memo))

for a in dates:
	bdate = (datetime.strptime(a, '%Y-%m-%dT%H:%M:%S'))
	now = datetime.now()
	age = (now-bdate)
#	for x in age:
#		x.append(int.strip(age))
#	print(age.days,file=open('dates.txt','a'))

with open('dates.txt','r') as f:
	text = f.read().splitlines()
	for line in text:
		x.append(line)

print(x)
print(y)

plt.scatter(x,y)
#plt.xlim(0,10)
#plt.ylim(0,10)

plt.title('Relationship Between Age in Day and Number of Mementos')
plt.xlabel('age in days')
plt.ylabel('number of mementos')

plt.show()
