### CHAPTER 4.3 MANIPULATING STRINGS WITH METHODS ###

# converting to uppercase:
# string.upper()

# converting to lowercase:
# string.lower()

# removing whitespace from left/right side of string:
# string.rstrip()
# string.lstrip()

# remove from both sides at once
# string.strip()

# checking if a string starts/ends with a substring (case sensitive)
# string.startswith("")
# string.endswith("")

# Recall: strings are immutable.
# String methods do not change the string itself, rather modify it to form
# an output. well that answers my question about why these things exist--they're
# not functions that return a specified output that changes the original value

### EXCERSIZE TIME ###

print("#1") # Excersize #1
animals = "Animals"
badger = "Badger"
bee = "Honey Bee"
hbadger = "Honey Badger"

print(animals.lower())
print(badger.lower())
print(bee.lower())
print(hbadger.lower())

print("\n#1.1, I wanted to do this")
list = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
print(list)
for animal in list:
    print(animal.lower())
# I'm so amazing

print("#2") # Excersize #2
for animal in list:
    print(animal.upper())

print("#3") # Excersize #3
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
list3 = [string1, string2, string3]
print(list3)
for item in list3:
    print(item.strip())

print("#4") # Excersize #4
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
list4 = [string1, string2, string3, string4]
for item in list4:
    print(item.startswith("be"))

print("#5") # Excersize #5
def starts_with_be(flist):
    for item in flist:
        if item.startswith("be") == True:
            print(item)
        else:
            













