import clusters

blognames,words,data=clusters.readfile('blogdata1rem.txt')
clust=clusters.hcluster(data)
clusters.printclust(clust,labels=blognames)

