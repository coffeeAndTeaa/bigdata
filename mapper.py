#!/usr/bin/env python

import sys
import os

dict = {}

with open('~/AFINN-en-165.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split()
		value = words.pop()
		key = " ".join(words)
		dict[key] = value 

file_name = os.getenv('map_input_file')
names = file_name.split('_')
name =  file_name[0]
word_number = 0
valence = 0
for line in sys.stdin:
	line = line.strip()
	words = line.split()

	for word in words:
		word_number += 1
		if word in dict:
			valence += int(dict[word])

valence = valence / (word_number / 1000.0)
print('%s\t%s' %(name, valence))
