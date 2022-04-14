### 6.1 what are functions ###

# functions are values that can be assigned to a variable
# eg you can define len = "a string"
# thereafter you would be unable to use len() as a function because it exists as var
# you can remove the var with del len
# del doesn't delete the value, rather it detaches the name from the value
# you need parenthesis to call the function
# when a function changes of affects something external it has a side effect
# print() doesn't return text as a value
# print() returns special value called None
# None is the returned value
# meanwhile the printed text is the side effect of print()


### 6.2 write your own functions ###

# functions have the function signature and the function body
# def function() is the function signature
# the indented everything else is the function body
# anything indented will be part of the function body even if there is a line in btwn
# after return is executed everything after that will be ignored

# document your functions with """ comments""" at the start of the function body

# see exercise in functions.py


### 6.4 run in circles ###

# infinite loops aren't inherently bad, they can be used to check for interactions with hardware
# one use for a while loop is to check whether a userinput meets some condition
num = float(input("Enter a positive number: "))

while num <= 0:
    print("That's not a positive number!:)
    num = float(input("Enter a positive number: "))

#? when should while or if be used to check for conditions

# range(n), where n is positive, returns the range of integers from 0 to n-1
# range(a, n), where a and n are positive, returns the range of integers from a to n-1
# nested loops
for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")

# see loop.py for exercise


### 6.6 understand scope in python ###
# you can't assign the same variable different values except in a function
# function body has local scope while everything outside has global scope
# LEGB rule for resolving scope
# Local, Enclosing, Global, Built-in
# built-in are like the existing functions











