from __future__ import with_statement
import csv
import operator
import statistics
from collections import Counter
import math

stdev = 0
Sum = 0
row_count = 0

with open('friendcountsorthd.csv') as f:
  f.readline()
  # Create the list of salaries 
  friendcount = {} 
  for line in f.readlines():
    friend, value, friendnum, self = line.split(',')
    value = int(value.strip())
    valu2 = float(value)
    friendnum = friendnum.strip()
    friend = friend.strip()
    friendcount = [value]
    Sum += valu2
    row_count += 1
    mean = sum(friendcount)
    n = float(len(friendcount))
    mean = Sum/row_count
    stdev += (valu2 - mean)**2
    stdev = math.sqrt(stdev/(row_count))
    print(friendcount,',',mean,',',n,',',Sum,',',row_count)
    print(friend,',',stdev,',',valu2)
#    print(friend, min(friendcount), max(friendcount), mean, stdev)


#self.groups.setdefault(key, []).append(val)
#    if friendcount in friend:
#      friendcount[friend].append(value)
#    else:
#      friendcount[friend] = [value]
#  for k,v in friendcount.items():
#    get_stats(k,v)  


'''
f = open('friendcountsorted.csv',"r")
average = 0
Sum = 0
row_count = 0
for row in f:
	for column in row.split(','):
		try:
			n=float(column)
			Sum += n
			row_count += 1
		except ValueError:
			print("Error -- ({}) Column({}) could not be converted to float!")
		average = Sum
f.close()
print('The sum is: ', average)
print('The row count is: ', row_count)
avg1 = average/row_count
print('The mean is: ', avg1)
'''

