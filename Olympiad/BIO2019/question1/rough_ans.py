"""
program that reads a positive integer up to 20 digits
output smalled palindromic number higher than the input

https://www.olympiad.org.uk/papers/2019/bio/bio19-exam.pdf
https://www.olympiad.org.uk/papers/2019/bio/bio19-marks.pdf

so originally I was going to do Q1a but this turned into just a palindrome check
so I looked at a sample solution and well
https://github.com/matthewelse/british-informatics-olympiad/blob/master/2019/q1.py
TIL I should learn to use python classes? either that or my computational thinking just isn't developed enough
or it might just be fine maybe I added too many redundancies.
TIL you can map a number in one line
TIL how to program a carrying algo

1. mirror the right side to the left side
2. while mirroring, check if the number has increased
3. if not, increase the middle (two) numbers
4. carry if number is a 9

halfway through I got help from Lucas. Thanks lucas
"""


def recv():
	while True:
		try:
			inp = input("input a positive integer (will only read up to 20 digits)\n> ")[:20]
			inp_int = int(inp)
			if inp_int<0:
				print("input must be a positive integer")
				continue
			break
		except ValueError:
			print("that's not an integer")
	return inp


def mirror(map, higher=False):
	# 1. mirror right to left
	print(f"beginning mirror of {map}")
	for l in range(len(map)//2): # iterative increasing, left half of map
		r = -(l + 1) # iterative decreasing, adjusting right
		print(f"mirroring: left index {l} is {map[l]} and right index {r} is {map[r]}")
		if map[l] > map[r]: # 2. check if number has increased
			print(f"number has increased, {higher}")
			higher = True
		elif map[l] < map[r]:
			higher = False
		map[r] = map[l]
	return map, higher


def add_one(list, index, carry=False): # index tells you where to add the 1
	for x in range(index, -1, -1):
		print(f"ADDONE: adding 1 to {x} {type(list[x])}")
		if list[x] == 9:
			print(f"list[x] is {list[x]}. carrying...")
			carry = True
			list[x] = 0
			continue
		carry = False
		list[x] += 1
		break
	if carry == True:
		list.insert(0,1)
	print(f"done adding {list}")
	return list


def next_palindrome(num, higher=False): # stop procrastinating the actual question

	# map numstring into a manipulatable list
	map = list(int(x) for x in num)
	map, higher = mirror(map)

	# 3. adjust mid
	if higher == False:
		print(f"higher found to be {higher}")
		if len(map) % 2 == 0: # even case
			m = len(map)//2-1 #index of the middle left number
			print(f"adjusting even mid: m is index {m} and {map[m]}")
		else: # odd case
			m = len(map)//2
			print(f"adjusting odd mid: m is index {m} and {map[m]}")
		map = add_one(map, m)
		map, higher = mirror(map)

	out = ''.join(str(i) for i in map)
	return out

def main():
	p = recv()
	print(next_palindrome(p))

while True: # repeat program
	main()
