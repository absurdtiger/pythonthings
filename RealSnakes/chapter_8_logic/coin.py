# 8.8 challenge: simulate a coin toss experiment

import random

def coin_flip():
	if random.randint(0, 1) == 0:
		return "heads"
	else:
		return "tails"

def trial():
	n = 0
	if coin_flip() == "heads":
		result = coin_flip()
		while result == "heads":
			result = coin_flip()
			n += 1
#			print(f"n is {n}")
	else:
		result = "tails"
		while result == "tails":
			result = coin_flip()
			n += 1
#			print(f"n is {n}")
	return n

def simulation(a):
	total = 0
	for x in range(a):
#		print(f"x is {x}")
		total += trial()
	average = total / a
	return average

print(simulation(10_000))


