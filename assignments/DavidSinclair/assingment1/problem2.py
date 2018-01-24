#!python3
#
#2.  Write a Python program that:
#  1. takes as a command line argument a web page
#  2. extracts all the links from the page
#  3. lists all the links that result in PDF files, and prints out
#     the bytes for each of the links.  (note: be sure to follow
#     all the redirects until the link terminates with a "200 OK".)
#  4. show that the program works on 3 different URIs, one of which
#     needs to be: 
#     http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html
#
#LIBRARIES NEED BY PYTHON FOR THIS PROGRAM
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import validators
import requests

#LIST the ARGUMENTS used to start this program
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

if len(sys.argv) == 2:
        url = sys.argv[1]
        print(url)
else:
	print("Wrong number of arguments!")
	print("Usage: python3 problem2.py http://<URL>")
	sys.exit()

#VERIFY THAT THE ARGUMENT IS VALID HTTP
print("Verifying that the URL is correct")

validators.url(url)
if not validators.url(url):
	print(url,"not valid")
	sys.exit()
else:
	print(url, "valid")

#Sets the webpage and open
#url = "http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html" 
html_page = urlopen(url)
#parses the webpage 
soup = BeautifulSoup(html_page, "html.parser")

#Creates the array for adding links and url4 to
links = []
url4 = []

#Parses the webpage and pulls out all the links
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
#	print(link.get('href'))
	links.append(link.get('href'))
#Prints the number of links and Counts the number of links
print("\nThe number of URL's is ",len(links),"\n")  
print(*links,sep='\n')


for index , url3 in enumerate(links):
#I want to see if the URL listed has another location and the file is actually a pdf
	resp = requests.get(url3)
#	print(url3,resp.headers['content-type']== 'application/pdf')
	if (resp.headers['content-type']=='application/pdf') == True:
#		print(url3, 'this is application/pdf')
		url4.append(url3)
#	else:
#		print(url3, 'this was not added')	

#print('\nThere is ',len(url4),' pdf files on the ',url,'webpage.\n')

matching = [s for s in url4]
print("\nThere is ",len(matching)," pdf files on the ",url,"webpage.\n")

#print(*matching,sep='\n')

for index , url2 in enumerate(matching):
#I want to open the URL listed in my list, get the header and print the content-legth
	resp = requests.get(url2)
	print(url2,"has a file size of ",resp.headers['content-length'],"bytes.")

