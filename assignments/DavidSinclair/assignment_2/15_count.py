import requests #used for url request information
import time	#used for time of day
import os	#used for search strings and removeing of string information
import sys	#used for search strings and removeing of string information
import fileinput	#used for search strings and removeing of string information
import re	#used for search strings and removeing of string information
import json	#used by memo and carbondate

#List of all the files that are created using programs written by David Sinclair
file=open('twitter_links.raw', 'r')
twitterlinks = file.read().split('\n')
file.close()

file=open('400.txt', 'r')
notfound = file.read().split('\n')
file.close()

file=open('300.txt', 'r')
redirlink = file.read().split('\n')
file.close()

file=open('200.txt', 'r')
urlcomp = file.read().split('\n')
file.close()

#file=open('everythingelse.txt', 'r')
#every = file.read().split('\n')
#file.close()

file=open('notvalidurl.txt', 'r')
notvalid = file.read().split('\n')
file.close()

file=open('300comp.txt', 'r')
comp300 = file.read().split('\n')
file.close()

file=open('300good.txt', 'r')
good300 = file.read().split('\n')
file.close()

file=open('300fails.txt', 'r')
fails300 = file.read().split('\n')
file.close()

file=open('300connectfail.txt', 'r')
con300 = file.read().split('\n')
file.close()

file=open('200comp.txt', 'r')
comp200 = file.read().split('\n')
file.close()

file=open('200clean.txt', 'r')
cleantwitterurl = file.read().split('\n')
file.close()

file=open('twitremove.txt', 'r')
twitremove = file.read().split('\n')
file.close()

file=open('twitonly.txt', 'r')
twitonly = file.read().split('\n')
file.close()

file=open('memgat.txt', 'r')
memgat = file.read().split('\n')
file.close()

file=open('carbdate.txt', 'r')
carbdate = file.read().split('\n')
file.close()

file=open('memento_404.txt', 'r')
mem404 = file.read().split('\n')
file.close()

file=open('memojson_fail.txt', 'r')
memjson = file.read().split('\n')
file.close()

file=open('b_date_memto.csv', 'r')
bdatememto = file.read().split('\n')
file.close()

file=open('b_date_no_memto.txt', 'r')
bdatenomemto = file.read().split('\n')
file.close()


print(len(twitterlinks)-1, "is the number of links from the orginal twitter search.")
print(len(notfound)-1, "is the number of urls with code greater than 400")
print(len(redirlink)-1, "is the number of urls with server codes between 300 and 399")
print(len(urlcomp)-1, "is the number of urls with server codes between 200")
#print(len(every), "is the number of urls that do not follow above")
print(len(notvalid)-1, "is the number of links that were not valid.")
#print(len(valid), "is the number of links that were valid.")
#print(len(cleantwitterurl), "is the number of urls with out duplicates")
#print(len(twitonly), "is the number of urls that had twitter.com")
#print(len(twitremove), "is the number of urls with twitter.com removed")
#print(len(memgat), "is the number of urls in memgat")
#print(len(carbdate), "is the number of urls in carbdate")
#print('MATH')
print(len(notvalid)+len(urlcomp)+len(redirlink)+len(notfound)-4, "is the total number of links gathered.")
print(len(notvalid)+len(urlcomp)+len(redirlink)+len(notfound)-len(twitterlinks)-3, "is the total number of links minus orginal twitter search")
#print('\n')
print(len(redirlink)-1, "is the number of urls with server codes between 300 and 399")
print(len(comp300)-1, "is the total number of redirects" )
print(len(good300)-1, "is the number of urls following the redirect urls  with server code 200")
print(len(fails300)-1, "is the number of urls following the redirect urls that did not produce code 200")
print(len(con300)-1, "is the number of urls following the redirect urls that gave connection failure")
#print('\nMATH')
print(len(good300)+len(fails300)+len(con300)-3, "is the total number of redirected links")
print(len(good300)+len(fails300)+len(con300)-len(redirlink)-4, "is the total number of redirected links minus redirect link")
print(len(good300)+len(fails300)+len(con300)-len(comp300)-4, "is the total number of redirected links minus 300 complete")
#print('\n')
print(len(urlcomp)-1, "is the number of urls with server codes between 200")
print(len(good300)-1, "is the total number of redirects" )
print(len(comp200)-1, "is the number of urls with server codes between 200 after adding both 200 and 300 redirects")
#print('\nMATH')
print(len(good300)+len(urlcomp)-2, "is the total number of 200 from both the 300 redirect links and the server 200 that did not have redirects.")
#print('\n')
print(len(comp200)-1, "is the number of urls with server codes between 200 after adding both 200 and 300 redirects")
print(len(cleantwitterurl)-1, "is the number of urls with out duplicates")
#print('\nMATH')
print(len(comp200)-len(cleantwitterurl)-2, "is the number of duplicates")
#print('\n')
print(len(twitonly)-1, "is the number of urls without twitter.com")
print(len(twitremove)-1, "is the number of urls with twitter.com")
#print('\nMATH')
print(len(cleantwitterurl)-len(twitonly)-2, "is the number of urls with twitter.com removed")
#print('\n')
print(len(memgat)-1, "is the number of urls in memgat")
print(len(carbdate)-1, "is the number of urls in carbdate")
#print('\nMATH')
#print('\n')
print(len(mem404)-1, "is the number of urls that responed with a 404 webpage")
print(len(memjson)-1, "is the number of JSON files that did not work")
#print('\nMATH')
print(len(memgat)-len(memjson)-2, "is the number of Mementos that produced correct JSON")
print(len(bdatememto)-2, "is the number of Mementos and Carbon dates")
print(len(bdatenomemto)-1, "is the number of Carbon dates that did not have memento files")

