import csv
import math
import operator
import string
from collections import Counter
from math import sqrt

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():
        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings:
                continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    # Divide each total score by total weighting to get an average
    rankings = [(score / totalSim[item], item) for (item, score) in
               scores.items()]
    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings

with open('/home/david/Documents/cs532/assignment6_draft/ml-100k/u.data') as tsv:
	for line in csv.reader(tsv, delimiter="\t"):
		rate = int(line[2])
		movie = int(line[1])
		user = line[0]
		if user == '409':
			print(user, movie, rate,file=open('409movie.txt','a'))
		if user == '455':
			print(user, movie, rate,file=open('455movie.txt','a'))
		if user == '72':
			print(user, movie, rate,file=open('072movie.txt','a'))
	#print(rankings)
