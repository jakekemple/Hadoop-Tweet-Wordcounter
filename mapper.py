#!/usr/bin/env python

import io
import sys
import string

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='ISO-8859-1')

for line in input_stream:
	line = line.strip()
	keys = line.split()
	for key in keys:
            for p in string.punctuation:
                key = key.replace(p, "")
                value = 1

            if (key):
                print( "%s\t%d" % (key, value) )
