import csv
import math
import operator
from collections import Counter
import string

def euclideanDistance(P, Q):
	if( len(P) != len(Q) ):
		return -1
	sumOfSquares = 0
	for i in range(0, len(P)):
		sumOfSquares += (P[i] - Q[i]) * (P[i] - Q[i])
	return math.sqrt(sumOfSquares)



P = [48,1,1] #My age + gender + occupation

with open('/home/david/Documents/cs532/assignment6_draft/ml-100k/u.user') as tsv:
	for line in csv.reader(tsv, delimiter="|"):
		if line[2] == "M":
			line[2] = '1'
		if line[2] == "F":
			line[2] = '2'
		if line[3] == "administrator":
			line[3] = '1'              
		if line[3] == "artist":
			line[3] = '2'
		if line[3] == "doctor":
			line[3] = 3
		if line[3] == "educator":
			line[3] = 4
		if line[3] == "engineer":
			line[3] = 5
		if line[3] == "entertainment":
			line[3] = 6
		if line[3] == "executive":
			line[3] = 7
		if line[3] == "healthcare":
			line[3] = 8
		if line[3] == "homemaker":
			line[3] = 9
		if line[3] == "lawyer":
			line[3] = 10
		if line[3] == "librarian":
			line[3] = 11
		if line[3] == "marketing":
			line[3] = 12
		if line[3] == "none":
			line[3] = 13
		if line[3] == "other":
			line[3] = 14
		if line[3] == "programmer":
			line[3] = 15
		if line[3] == "retired":
			line[3] = 16
		if line[3] == "salesman":
			line[3] = 17
		if line[3] == "scientist":
			line[3] = 18
		if line[3] == "student":
			line[3] = 19
		if line[3] == "technician":
			line[3] = 20
		if line[3] == "writer":
			line[3] = 21
		Q = [int(line[1]),int(line[2]),int(line[3])]
		print(line[0], euclideanDistance(P, Q),file=open('dist_user.txt','a'))


#import math
#def euclideanDistance(P, Q):
#
#	if( len(P) != len(Q) ):
#		return -1
#
#	sumOfSquares = 0
#	for i in range(0, len(P)):
#		sumOfSquares += (P[i] - Q[i]) * (P[i] - Q[i])
#
#	return math.sqrt(sumOfSquares)
#
#P = [48, 0, 1]
#Q = [48, 0, 2]
#
#print( euclideanDistance(P, Q) )	
#
#
#with open('output', 'w') as f:
#    f.write('\t'.join(l[1:]) + '\n')
#print(numline)
#print(r)

#lines = list(f)
#for n, i in enumerate(lines):
#	print(i)
#	if i == "M":
#		lines[n] = 1
#		print(lines)
#for index, item in enumerate(items):
#   ...:     if not (item % 2):
#   ...:         items[index] = None

#   v = open(input.csv)
#    r=csv.reader(v)
#    numline = len(v.readlines())
#    print (numline)
#    for row in r:
#        if row["Baby"] == "Baby":
#            for i in range (1, numline):
#                print("test")
'''
for row in f:
	for column in row.split('|'):
		if column == "M":
			column = 1
		if column == "F":
			column = 2
		if column == "administrator":
                        column = 1		
		if column == "artist":
                        column = 2
		if column == "doctor":
                        column = 3
		if column == "educator":
                        column = 4
		if column == "engineer":
                        column = 5
		if column == "entertainment":
                        column = 6
		if column == "executive":
                        column = 7
		if column == "healthcare":
                        column = 8
		if column == "homemaker":
                        column = 9
		if column == "lawyer":
                        column = 10
		if column == "librarian":
                        column = 11
		if column == "marketing":
                        column = 12
		if column == "none":
                        column = 13
		if column == "other":
                        column = 14
		if column == "programmer":
                        column = 15
		if column == "retired":
                        column = 16
		if column == "salesman":
                        column = 17
		if column == "scientist":
                        column = 18
		if column == "student":
                        column = 19
		if column == "technician":
                        column = 20
		if column == "writer":
                        column = 21
#		print(column,file=open('u.usermod','a'))


m=1
f=2

administrator
artist
doctor
educator
engineer
entertainment
executive 
healthcare
homemaker
lawyer
librarian
marketing
none
other
programmer
retired
salesman
scientist
student
technician
writer

'''
