import clusters

blognames,words,data=clusters.readfile('blogdata1rem.txt') 
kclust=clusters.kcluster(data,k=10)
print([blognames[r] for r in kclust[0]])
print([blognames[r] for r in kclust[1]])
print([blognames[r] for r in kclust[2]])
print([blognames[r] for r in kclust[3]])
print([blognames[r] for r in kclust[4]])
print([blognames[r] for r in kclust[5]])
print([blognames[r] for r in kclust[6]])
print([blognames[r] for r in kclust[7]])
print([blognames[r] for r in kclust[8]])
print([blognames[r] for r in kclust[9]])