import boilerpipe
from boilerpipe.extract import Extractor
import os, os.path
import re

# simple version for working with CWD
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

# path joining version for other paths
DIR ='/home/david/Documents/cs532/assignment3_draft/html/'
DIR2 = '/home/david/Documents/cs532/assignment3_draft/processed/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

for file in os.listdir(DIR):
	if file.endswith(".html"):
#		print(os.path.join(DIR, file))
		print(file,file=open('htmlnames.txt','a'))
	
with open('htmlnames.txt') as f:
    text = f.read().splitlines()
for file in text:
	try:
		filename=DIR+file
	#	print(filename)
		x = open(filename)
	#	print(x)
		html = x.read()
	#	print(html)
		extractor = Extractor(extractor='ArticleExtractor', html=html)
		processed = extractor.getText()
		newfile = re.sub('html', 'txt', file)
		newfileloc = DIR2+newfile
		print(processed,file=open(newfileloc,'w'))
	except UnicodeDecodeError:
		print("UnicodeDecodeError.",file,file=open('ErrorProcessing.txt','a'))
	except Exception:
		print("No Text.",file,file=open('NotextProcessing.txt','a'))
