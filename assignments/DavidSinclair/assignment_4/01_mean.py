import csv
import operator
from collections import Counter

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

