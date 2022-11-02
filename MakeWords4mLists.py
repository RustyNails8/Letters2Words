#! <python3.10>
# Sumit Das

from textblob import Word
import sys

try:
	myWORD=sys.argv[1]
	myLetters=list(myWORD)
	LENGTH=sys.argv[2]
	# print("My Words is : " + str(myWORD) + " and Number of letters is " + str(LENGTH))
	# print(myLetters)
except:
	LENGTH=0

def has_all(chars, string):
    return all([char in string for char in chars])

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		if len(lines[i]) == int(LENGTH) :
			word = Word(str(lines[i]))
			result = word.spellcheck()
			if result[0][1] == 1.0 :
				if int(LENGTH) == 0:
					print(result[0][0])
				else:
					if len(result[0][0]) == int(LENGTH) :
						newWord=result[0][0]
						# print(has_all(newWord, myLetters))
						if (has_all(newWord, myLetters)):
							# print(result[0][0])
							print(newWord)
			
f.close()