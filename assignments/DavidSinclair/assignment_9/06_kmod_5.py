import modclusters

blognames,words,data=modclusters.readfile('blogdata1rem.txt') 
kclust=modclusters.kcluster(data,k=5)
print([blognames[r] for r in kclust[0]],kclust[0])
print([blognames[r] for r in kclust[1]],kclust[1])
print([blognames[r] for r in kclust[2]],kclust[2])
print([blognames[r] for r in kclust[3]],kclust[3])
print([blognames[r] for r in kclust[4]],kclust[4])
