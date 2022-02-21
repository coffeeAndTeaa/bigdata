#!/usr/bin/env python

import sys
dict = {}

with open('./AFINN-en-165.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split()
		value = words.pop()
		key = " ".join(words)
		dict[key] = value 

for line in sys.stdin:
	line = line.strip()
	words = line.split()

	for word in words:
		if word in dict:
			print('%s\t%s' %(word, dict[word]))
