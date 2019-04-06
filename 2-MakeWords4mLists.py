#! <python3.7>
# Sumit Das

import enchant
D = enchant.Dict("en_US")

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		myCHECK = D.check(lines[i])
		if myCHECK:
			if len(lines[i]) > 2:
				print(lines[i])
				D.suggest(lines[i])

f.close()