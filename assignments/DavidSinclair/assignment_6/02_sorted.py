import csv
import operator


sample = open("dist_user.txt")
csv1 = csv.reader(sample, delimiter=' ')
#sort = sorted(csv1, key=operator.itemgetter(1))
sort = sorted(csv1, key=lambda x : (x[1]))
for eachline in sort:
    print(eachline)
