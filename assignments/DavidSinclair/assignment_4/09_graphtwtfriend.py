import operator
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from statistics import median
import math

stdev = 0
x = [0,1,1,1,5,11,15,36,48,73,77,85,96,114,122,141,142,165,183,184,185,251,271,277,283,294,304,313,318,341,368,376,400,419,421,434,437,440,464,496,501,503,555,582,604,661,753,758,760,818,824,893,897,955,957,967,985,1056,1060,1130,1274,1298,1677,1682,1689,1856,2090,2309,2722,2963,3133,3281,3341,3871,4512,6302,9866]

mean = np.mean(x)
y = max(x)
anwala = 77 
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
plt.plot([55],mean,marker='x',markersize=3, color='red',label='Mean = 1021.8')
plt.plot([53],stdev,marker='x',markersize=3, color='blue',label='Standard Deviation = 1007.892')
plt.plot([34],med,marker='x',markersize=3, color='green',label='Median = 464')
plt.plot([11],anwala,marker='x',markersize=3, color='yellow',label='Anwala = 77')
plt.legend()
plt.ylabel('Friend Count')
plt.xlabel('Friends')
plt.show()

