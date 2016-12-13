"""
Serial program to count words from a text file
Usage: python serial-wordcount.py <filename>
"""

import sys
import string

#Open file
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

wordcounts = dict()

for line in lines:
    line = line.strip()
    words = line.split()
    for word in words:
        #Remove punctuation
        for p in string.punctuation:
            word = word.replace(p, "")
        #Add word to dictionary
        if (word != ""):  #skip counts for empty string
            if (word not in wordcounts):
                wordcounts[word] = 1
            else:
                wordcounts[word] += 1

#Get sorted list of words
keys = [(k, wordcounts[k]) for k in sorted(wordcounts, key=wordcounts.get, reverse=True)]

#Print each word with its count
with open('serial_sorted.txt','a') as tf:
    for key, v in keys:
        tf.write("%s\t%d\n" % (key, wordcounts[key]))
