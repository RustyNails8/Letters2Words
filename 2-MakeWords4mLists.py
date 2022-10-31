#! <python3.10>
# Sumit Das

from textblob import Word
import sys

try:
	LENGTH=sys.argv[1]
except:
	LENGTH=0

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		if len(lines[i]) == int(LENGTH) :
			word = Word(str(lines[i]))
			result = word.spellcheck()
			if result[0][1] == 1.0 :
				if LENGTH == 0:
					print(result[0][0])
				else:
					if len(result[0][0]) == int(LENGTH) :
						print(result[0][0])
				
f.close()