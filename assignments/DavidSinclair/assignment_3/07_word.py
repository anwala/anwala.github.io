import os, os.path
import re
import re
from collections import Counter

wanted = 'government'
cnt = Counter()

# simple version for working with CWD
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

# path joining version for other paths
DIR = '/home/david/Documents/cs532/assignment3_draft/processed/'
dirpath = '/home/david/Documents/cs532/assignment3_draft/processed/'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

for file in os.listdir(DIR):
	if file.endswith(".txt"):
#		print(os.path.join(DIR, file))
		print(file,file=open('txtnames.txt','a'))
	
with open('txtnames.txt') as f:
    text = f.read().splitlines()
for name in text:
	filename=DIR+name
	print(filename)
'''
	if 'minister' in open(filename).read():
		print("true")
		words = re.findall('\w+',open(filename).read().lower())
		for word in words:
			if word in wanted:
				cnt[word] += 1
				print(cnt)
'''
import glob

def word_frequency(fileobj, words):
    """Build a Counter of specified words in fileobj"""
    # initialise the counter to 0 for each word
    ct = Counter(dict((w, 0) for w in words))
    file_words = (word for line in fileobj for word in line.split())
    filtered_words = (word for word in file_words if word in words)
    return Counter(filtered_words)


def count_words_in_dir(dirpath, words, action=None):
    """For each .txt file in a dir, count the specified words"""
    for filepath in glob.iglob(os.path.join(dirpath, '*.txt')):
        with open(filepath) as f:
            ct = word_frequency(f, words)
            if action:
                action(filepath, ct)


def print_summary(filepath, ct):
    words = sorted(ct.keys())
    counts = [str(ct[k]) for k in words]
    print('{0}\n{1}\n{2}\n\n'.format(
        filepath,
        ', '.join(words),
        ', '.join(counts)))


words = set(['government', 'Trump', 'justice', 'the', 'minister', 'congress'])
count_words_in_dir('./', words, action=print_summary)
