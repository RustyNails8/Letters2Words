#! <python3.10>
# Sumit Das

from textblob import Word
import sys

try:
	# Useage of script
	# python MakeWords4mLists.py boko 4
	# python MakeWords4mLists <jumbled word/letters> <number of letters>

	# Stoarge original jumbled word in myWORD
	myWORD=sys.argv[1]

	# Break myWORD into a list of letters
	# r n c a t o o
	# myLetter[0] = r
	# myLetter[1] = n
	# ...
	# etc.
	myLetters=list(myWORD)

	# This stores the number of letters
	LENGTH=sys.argv[2]
	# print("My Words is : " + str(myWORD) + " and Number of letters is " + str(LENGTH))
	# print(myLetters)
except:
	LENGTH=0

# Defined a Function to check if a word contains a set of characters
# Ref: 
def has_all(chars, string):
    return all([char in string for char in chars])

# Open the text file which contains all the possible combinations 
# ... that are possible from letters of jumbed word - myWORD
# ... and each of this line / word should be checked if it is a dictionary word
# ... We can call each line as word candidate !
# TODO Rewrite this portion in python and remove C++ depndency

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		# Check if the word candidate is of defined lenght
		if len(lines[i]) == int(LENGTH) :
			# If yes, spellcheck 
			word = Word(str(lines[i]))
			result = word.spellcheck()
			# Check if word candidate has 100% confidence
			if result[0][1] == 1.0 :
				if int(LENGTH) == 0:
					# Exception handling, when someone did not provide lenght of word
					print(result[0][0])
				else:
					# Agian Check if the word candiate is of defined lenght 
					# We  need to do this as textblob may reduce number of letters
					if len(result[0][0]) == int(LENGTH) :
						# Store word candidate in newWord
						newWord=result[0][0]
						# print(has_all(newWord, myLetters))
						# Check if newword has all the letters as in original jumbled word - myWORD
						# TODO : Need help here
						if (has_all(newWord, myLetters)):
							# print(result[0][0])
							print(newWord)
			
f.close()