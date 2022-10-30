#! <python3.10>
# Sumit Das

from textblob import Word

# import enchant
# D = enchant.Dict("en_US")

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		word = Word(str(lines[i]))
		result = word.spellcheck()
		if [ result[0][1] == 1.0 ]:
			if [ len(result[0][0]) == len(lines) ]:
				print(result[0][0])

		# myCHECK = D.check(lines[i])
		# if myCHECK:
		# 	if len(lines[i]) > 2:
		# 		print(lines[i])
		# 		D.suggest(lines[i])

f.close()