# 8.9 challenge simulate an election

import random

percentages = [0.87, 0.65, 0.17]

def regional_elections():
	wins = 0
	for region in percentages:
		if random.random() <= region:
			wins += 1
	if wins >= 2:
		return "president"

def simulate(a):
	president = 0
	for x in range(a):
		if regional_elections() == "president":
			president += 1
	average = president / a
	print(f"percentage is {average:.2%}")

simulate(10_000)






