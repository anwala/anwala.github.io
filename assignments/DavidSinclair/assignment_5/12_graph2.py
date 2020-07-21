import networkx as nx
from matplotlib import pylab as pl
from operator import itemgetter

def edge_to_remove(G):
	dict1 = nx.edge_betweenness_centrality(G)
	list_of_tuples = dict1.items()
	list_of_tuples=sorted(list_of_tuples, key=lambda x:x[1], reverse=True)
	for x in list_of_tuples:
		return x[0]	

def girvan(G):
	c = nx.connected_component_subgraphs(G)
	l = len(list(c))
	pos = nx.spring_layout(G)
	count = 1
	print(count," The number connected compents are ",l)
	output = "karate%(id)02d.png" % {"id": count}
	print('The file # is ', count,' Edge that was removed: ',edge_to_remove(G), file=open('edgeremove.txt','a'))
	pl.figure()
	nx.draw_networkx(G, pos)
	pl.savefig(output)
	pl.close()	
	while(l < 5):
		G.remove_edge(*edge_to_remove(G)) #((a,b)) --> (a,b)
		c = nx.connected_component_subgraphs(G)
		l = len(list(c))
		pos=nx.spring_layout(G)
		count +=1
		print(count, " The number connected compents are ",l)
		print(nx.number_of_nodes(G))
		print('The file # is ', count,' Edge that was removed: ', edge_to_remove(G),file=open('edgeremove.txt','a'))
		output = "karate%(id)02d.png" % {"id": count}
		pl.figure()
		nx.draw_networkx(G)   
		pl.savefig(output)
		pl.close()

	return c

G = nx.karate_club_graph()
count = 0
pos = nx.spring_layout(G)
output = "karate%(id)02d.png" % {"id": count}
print('The file # is ', count,file=open('edgeremove.txt','a'))
pl.figure()
nx.draw_networkx(G, pos)
pl.savefig(output)
pl.close()
c = girvan(G)
