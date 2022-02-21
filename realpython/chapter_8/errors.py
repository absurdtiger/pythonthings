# 8.6 recover from errors

# program that repeatedly asks for integer input, if the user enters something
# other than an integer, the program should catch the ValueError and display
# "try again"

def repeat():
	try:
		i = 0
		while i == 0:
			thing = int(input("gimme an integer rn u dum shit: ")
		except ValueError:
			print("I said integer u dum shit")
			continue
		break
	print(f"you entered {thing} thanks u smort shit")


repeat()
