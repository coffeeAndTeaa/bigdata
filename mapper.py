import sys
dict = {}

with open('./AFINN-en-165.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		(key, value) = line.split()
		dict[key] = value 

for line in sys.sidin:
	line = line.strip()
	words = line.split()

	for word in words:
		if word in dict:
			print('%s\t%s' %(word, dict[word]))
