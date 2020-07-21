import operator
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from statistics import median
import math

stdev = 0
x = [0,0,1,2,2,2,4,4,4,6,6,7,7,9,10,11,13,13,13,15,15,17,18,19,19,20,20,20,21,21,22,23,26,26,32,32,33,34,36,36,38,38,41,41,42,42,42,42,46,50,53,53,55,56,57,64,74,79,82,91,94,96,106,113,115,122,123,130,135,143,144,147,151,152,152,153,156,169,175,188,192,200,201,203,210,215,227,227,236,244,245,259,261,262,265,270,277,290,292,307,320,322,323,330,358,366,370,378,387,392,411,423,429,433,435,455,477,477,515,526,546,567,567,576,598,600,611,636,705,726,743,746,750,759,827,841,852,928,969,1017,1038,1073,1081,1118,1139,1146,1197,1248,1291,1305,1416,1443,1502,1509,1520,1528,1537,1663,1704,1753,1776,1825,1828,1832,1910,2023,2034,2054,2062,2120,2162,2444,2526,2616,2827,3535,3641,3981,4305,4362,4399,5165,5241,7015,8420,8934,23895,42611,45240,46264,51001,53951,170109]

mean = np.mean(x)
y = max(x)
anwala = 192 
count = len(x)
stdev += ((y) - mean)**2
stdev = math.sqrt(stdev/count)
med = median(x)
print(y)
print(anwala)
print(stdev)
print(med)
print(mean)
plt.plot(x)
plt.plot([175],mean,marker='x',markersize=3, color='red',label='Mean = 3022.6')
plt.plot([185],stdev,marker='x',markersize=3, color='blue',label='Standard Deviation = 12027.142')
plt.plot([100],med,marker='x',markersize=3, color='green',label='Median = 277')
plt.plot([78],anwala,marker='x',markersize=3, color='yellow',label='Anwala = 192')
plt.legend()
plt.ylabel('Followers Count')
plt.xlabel('Followers')
plt.show()

