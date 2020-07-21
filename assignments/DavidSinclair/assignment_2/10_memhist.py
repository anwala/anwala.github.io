import matplotlib.pyplot as plt
import re
from collections import Counter
import operator  # Used tor sorting
from itertools import groupby

count=0

file=open('histograph.data', 'r')
hist = file.read().split('\n')
file.close()

with open('histograph.data') as f:
	data = f.read().splitlines()
	print(len(data))
	print(len(set(data)))
	data_1 = sorted(data, key=int)
	bin_count = len(set(data))
	data_set = set(data)
	print(data_set)
	data_sort = sorted(data_set, key=int)
	print(data_sort)
	print([len(list(group)) for key, group in groupby(data_1)])

fin = [data_sort.index(i) for i in data]
plt.hist(fin, bins=bin_count, align="left")
plt.xticks(range(28), data_sort)

plt.title("Historgram Plot of Memo")
plt.xlabel("Number of mementos")
plt.ylabel("frequuency of occurence")
plt.show()

