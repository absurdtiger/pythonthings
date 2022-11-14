"""
How many integers are there, between 1 and 99999 inclusive, that are not the sum of two palindromic numbers?
er
sums of palindromes might not be palindromes
I think this is going to take too long to compute
iteratively, a + b, where a and b are palindromes from 1 to 99999, to get a list of numbers
or could do it the other way round. generate numbers from 1 to 99999, then check for palindromes based on iterative check
"""
from clean import next_palindrome as program

ints = []
pals = [1]
notsum = []
for i in range(99999):
	ints.append(i+1) # generate list of numbers

for i in range(99999):
	if program(i) <= 99999:
		pals.append(program(i))
	else: break

for item in ints:
	print(f"checking {item}")
	for a in pals:
		if a >= item:
			break
		for b in pals:
			if item == a + b or b + a >= item:
				break
	notsum.append(item)

print(len(notsum))
