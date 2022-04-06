# 8.5 break out of the pattern

# 'continue' skips the iteration in the loop (outside of any if loop)
# 'break' stops the loop and else loops from running

def orange():
	i = 0
	while i == 0:
		fruit = input("Give me some input: ")
		if fruit.find("Q") != -1 or fruit.find("q") != -1:
			i += 1
			break

# orange()


def apple():
	print("Printing all numbers from 1 to 50 that are not multiples of 3:")
	for x in range(51):
		if x % 3 == 0:
			continue
		print(x)

# apple()
