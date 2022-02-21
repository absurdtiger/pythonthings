# 8.6 recover from errors

# program that repeatedly asks for integer input, if the user enters something
# other than an integer, the program should catch the ValueError and display
# "try again"

# always use try inside while, not the other way round

def repeat():
	while True:
		try:
			thing = int(input("gimme an integer rn u dum shit: "))
			print(f"you entered {thing} thanks u smort shit")
			break
		except ValueError:
			print("I said integer u dum shit")

# repeat()

def string():
	while True:
		try:
			input1 = input("Give me a string: ")
			input2 = int(input("Give me an integer: "))
			print(f"{input1[input2]}")
			break
		except ValueError:
			print("INTEGER")
		except IndexError:
			print("Your integer was out of bounds")

string()
