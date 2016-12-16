#!/usr/bin/env python

import io
import sys
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='ISO-8859-1')

word_dict = {}

for line in input_stream:
    line = line.strip()
    key, value = line.split("\t", 1)
    value = int(value)

    if key not in word_dict:
        word_dict[key] = value
    else:
        word_dict[key] += value

#Get sorted list of keys
keys = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)]

#Print each word with its count
for k, v in keys:
    print("%s\t%d" % (k, word_dict[k]))
