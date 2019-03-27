#!/opt/conda/bin/python

# import sys and os for command-line functionality
import sys
import os
# letter library for wordcount search
import string

# define input filename since used more than once
fname = sys.argv[1]

# create output file. split for readability
fout = os.path.join(os.getcwd(),fname+'_letercount.txt')
sys.stdout = open(fout,'w')

# read in words and create list
wordList = open(fname).read().splitlines()

# matching routine to count letter instances
# (same as in homework .ipynb)
for i in string.ascii_lowercase:
	count=0
	for word in wordList:
		if word[0].lower() == i:
			count = count + 1
	print(i,count)
