import docclass
from subprocess import check_output
import os, os.path

path ='/home/david/Documents/cs532/assignment8_draft/train/'

with open('01names.txt') as f:
#with open('/home/david/Documents/cs532/assignment8_draft/train/nonspam1.txt') as f:
    text = f.read().splitlines()
for name in text:
    filename=path+name             
    with open(filename) as f:
       doc = f.read()
#doc = docclass.naivebayes(docclass.getwords)
       cl = docclass.naivebayes(docclass.getwords)
#remove previous db file
       check_output(['rm', 'spam.db'])
       cl.setdb('spam.db')
       docclass.spamTrain(cl)
       #classify text: "the banking dinner" as spam or not spam
       print(filename, cl.classify(doc))

