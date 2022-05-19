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
# 8.6 recover from errors

# listing the types of errors
# ValueError
# 	when the operation encounters an invalid value, such as converting a string to an integer
# TypeError
# 	when operation is performed on wrong value
# 	e.g. trying to add a string and int
# NameError
# 	when var name hasn't been defined
# ZeroDivisionError
# 	when divisor is 0
# OverflowError
# 	when result of math is too large

# if you anticipate an exception to occur, you can catch the error

# or you can use except (ExampleError, AnotherExampleError):
# you can write multiple except blocks after try
# ON THE SAME DAMN INDENT
# one big problem I made was not closing int(input("") yeahh you need 2 closing brackets

# if error is unspecified, any error at all will execute except

