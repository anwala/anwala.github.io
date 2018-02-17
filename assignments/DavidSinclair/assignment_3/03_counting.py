import os, os.path
import re

# simple version for working with CWD
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

# path joining version for other paths
DIR ='/home/david/Documents/cs532/assignment3_draft/html/'
DIR2 = '/home/david/Documents/cs532/assignment3_draft/processed/'
print('html directory count: ',len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print('processed director count: ',len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))]))

file=open('uri.raw', 'r')
uri = file.read().split('\n')
file.close()

file=open('htmlnames.txt', 'r')
html = file.read().split('\n')
file.close()

file=open('NotextProcessing.txt', 'r')
notext = file.read().split('\n')
file.close()

file=open('ErrorProcessing.txt', 'r')
error = file.read().split('\n')
file.close()

file=open('minwordcount.txt', 'r')
minwo = file.read().split('\n')
file.close()


print(len(uri), " is the number of uri files.")
print(len(html), " is the number of html files.")
print(len(notext), " is the number of htmls that had no text in them.")
print(len(error), " is the number of htmls that had errors in decoding.")
print(len(minwo), " is the number of ministers in the files.")

