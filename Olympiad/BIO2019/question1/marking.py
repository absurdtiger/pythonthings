from clean import next_palindrome as program

a = open('test_inputs.txt', 'r')
inp = []
for line in a:
	inp.append(line.strip())
a.close()

b = open('answers.txt', 'r')
answer = []
for line in b:
	answer.append(line.strip())
b.close()

score = 0
total = 0

for y in range(len(inp)):
	total += 1
	output = program(inp[y])
	if output == answer[y]:
		print(f"{y+1}) {inp[y]} --> {output} | {answer[y]} correct")
		score += 1
	else:
		print(f"{y+1}) {inp[y]} --> {output} | {answer[y]} wrong")

print(f"score: {score}/{total}")
