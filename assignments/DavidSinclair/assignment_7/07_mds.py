import clusters

blognames,words,data=clusters.readfile('blogdata1rem.txt') 
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')
