# 8.3 control the flow of your program

def five_chars():
	word = input("give me a word: ")
	if len(word) < 5:
		print("Your input is less than 5 characters long")
	elif len(word) > 5:
		print("Your input is gretaer than 5 characters long")
	else :
		print("Your input is 5 characters long")

five_chars()

def guess():
	number = int(input("I'm thinking of a number between 1 and 10. Guess which one."))
	if number == 3:
		print("You win!")
	else :
		print("You lose.")

guess()
