# 8.4 challenge: find the factors of a number

x = int(input("Enter a positive integer: "))
n = 1
if x <= 0:
	print("I said positive integer you ass")
else:
	while n <= x:
		if (x % n) == 0:
			print(f"{n} is a factor of {x}")
			n += 1
		else:
			n+=1
			continue



