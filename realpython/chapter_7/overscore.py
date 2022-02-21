# to remove underscores

def rem_underscores(word):
	n = word.find("_")
	if n == -1:
		print("Your input does not have any underscores.")
		return "<invalid>"
	while n != -1:
		word = word[:n] + word[n+1:]
		n = word.find("_")
	return word

def overscore(word):
	word = word.replace("_","")
	return word

input = input("Enter a word with underscores: ")
output = rem_underscores(input)
print(f"Your output is {output}")

print(f"Your alternative output is {overscore(input)}")


