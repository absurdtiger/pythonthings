from clean import next_palindrome as program

# main purpose of this program is to observe differences. would take too long to actually find the ans for 2m
largest = 99999999999999999999
largest_diff = 0
for i in range(largest):
	out = program(str(i))
	diff = int(out)-i
	if diff > largest_diff:
		largest_diff = diff
		print(f"new largest diff at {i} giving {out} and diff {diff}")

print(f"found! {largest_diff}")
