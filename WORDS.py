#! <python3.7>
# Sumit Das

import enchant


# f = open("WORDS.TXT", "r")

D = enchant.Dict("en_US")

"""for line in f:
	myLINE = f.readline()
	# print(f.readline())
	# print(line)
	# myCHECK = D.check(myLINE)
	# print(myCHECK)
	# if myCHECK == True:
	#   print(line)
	print(D.suggest(line))"""

with open('WORDS.TXT') as f:
    lines = f.read().splitlines()

i = 0
for i in range(0,len(lines)):
	if lines[i]:
		myCHECK = D.check(lines[i])
		if myCHECK:
			print(lines[i])
			D.suggest(lines[i])

f.close()