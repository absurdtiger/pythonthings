# 8.7 simulate events and calculate probabilities

# for random numbers you have to import the random module
import random
# random.randint(1, 10)
# MODULES ARE NOT LIBRARIES

def coin_flip():
	if random.randint(0, 1) == 0:
		return "heads"
	else:
		return "tails"

heads_tally = 0
tails_tally = 0

for trail in range(10_000):
	if coin_flip() == "heads":
		heads_tally += 1
	else:
		tails_tally += 1

# random() takes no arguments and returns a float >= 0.0 but < 1.0

def roll():
	die = random.randint(1, 6)
	return die

print(roll())

def average():
	total = 0
	n = 0
	for trial in range(10_000):
		total += roll()
		n += 1
		print(f"total is {total} and n is {n}")
	average = total / n
	return average

print(average())
