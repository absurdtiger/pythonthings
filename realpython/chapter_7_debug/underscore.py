# im doing this for fun

def add_underscores(word):
	new_word = "_"
	for letter in word:
		new_word = new_word + letter + "_"
	return new_word

input = input("enter a word: ")
output = add_underscores(input)
print(f"Your underscored word is {output}")
