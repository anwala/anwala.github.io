import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import validators
import requests


fin = open("blogurl.txt")
fout = open("urlclean.txt", "w+")
delete_list = ['?expref=next-blog']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('urlclean.txt', 'r') as istr:
    with open('blogclean.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + 'feeds/posts/default'
            print(line, file=ostr)

print('done')
