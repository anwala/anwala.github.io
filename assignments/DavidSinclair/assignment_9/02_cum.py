import numpredict
import clusters

vec2,high,data=clusters.readfile('blogdata1rem.txt')
vec1 ='F-Measure'
print(data)
print(numpredict.cumulativegraph(data,vec1,))
