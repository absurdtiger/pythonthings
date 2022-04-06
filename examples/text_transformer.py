print("""
WELCOME TO THE PYTHON

████████╗███████╗██╗░░██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░
░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░
░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

████████╗██████╗░░█████╗░███╗░░██╗░██████╗███████╗░█████╗░██████╗░███╗░░░███╗███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝██╔══██╗
░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░█████╗░░██║░░██║██████╔╝██╔████╔██║█████╗░░██████╔╝
░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""")

# global string
string = ""


# DECLARE REPEAT

def repeat():
    repeat = input("""
Would you like to:
1. Change string
2. Keep string
3. Exit
> """)
    if repeat == '1':
        main()
    elif repeat == '2':
        action()
    elif repeat == '3':
        exit()
    else:
        print("\nvalid option please")
        repeat()


# FUNCTIONS

def uppercase(a):
    upper = a.upper()
    print("\nYour uppercase string is:\n" + upper)
    repeat()


def lowercase(a):
    lower = a.lower()
    print("\nYour lowercase string is:\n" + lower)
    repeat()


# MAIN

def main():
    global string
    string = input("\nEnter a string:\n> ")
    action()


def action():
    operation = input("""
What operation would you like to perform?

1. Turn a string into uppercase
2. Turn a string into lowercase
3. Add underscores between each character


> """)
    if operation == '1':
        uppercase(string)
    elif operation == '2':
        lowercase(string)
    elif operation == '3':
        print("what should I put here though?")
        action()
    else:
        print("\nEnter a valid option!")
        action()


# Initialise
main()
