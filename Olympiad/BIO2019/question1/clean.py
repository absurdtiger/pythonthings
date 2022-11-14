"""
program that reads a positive integer up to 20 digits
output smalled palindromic number higher than the input
"""


def recv():
	while True:
		try:
			inp = input()[:20]
			inp_int = int(inp)
			if inp_int<0:
				print("input must be a positive integer")
				continue
			break
		except ValueError:
			print("that's not an integer")
	return inp_int


def mirror(map, higher=False):
	for l in range(len(map)//2): # iterative increasing, left half of map
		r = -(l + 1) # iterative decreasing, adjusting right
		if map[l] > map[r]: # 2. check if number has increased
			higher = True
		elif map[l] < map[r]:
			higher = False
		map[r] = map[l]
	return map, higher


def add_one(list, index, carry=False): # index tells you where to add the 1
	for x in range(index, -1, -1):
		if list[x] == 9:
			carry = True
			list[x] = 0
			continue
		carry = False
		list[x] += 1
		break
	if carry == True:
		list.insert(0,1)
	return list


def next_palindrome(num_int, higher=False):
	num = str(num_int)
	map = list(int(x) for x in num)
	map, higher = mirror(map)
	if higher == False:
		if len(map) % 2 == 0: # even case
			m = len(map)//2-1 #index of the middle left number
		else: # odd case
			m = len(map)//2
		map = add_one(map, m)
		map, higher = mirror(map)
	out = int(''.join(str(i) for i in map))
	return out


def main():
	p = recv()
	print(next_palindrome(p))


if __name__ == '__main__':
	main()
