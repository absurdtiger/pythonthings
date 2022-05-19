# testing the proposed answer to the errors exercise

while True:
    try:
        my_input = input("Type an integer: ")
        print(int(my_input))
        break
    except ValueError:
        print("try again")

while True:
	try:
		thing = int(input("say something: "))
		break
	except ValueError:
		print("nope")
