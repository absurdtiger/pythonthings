### 4.8 Find a String in a String ###

# .find() returns the index of the first occurence of the string
# python indexes start from 0
# if substring is not found, it will return -1
# matching is case sensitive
# .find() is only for strings

# .replace("string1", "string2")
# where string1 is to be replaced by string2

# Ex1
print("AAA".find("a"))

# Ex2
string = "Somebody said something to Samantha."
new_string = string.replace("s", "x")
print(new_string)

# Ex3
yes = input("input something pls")
print("The letter a is at " + str(yes.find("a")))
