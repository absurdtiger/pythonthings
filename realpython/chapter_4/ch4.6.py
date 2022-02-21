### 4.6 Working with Strings and Numbers ###

thing = "5"
actual_thing = int(thing)
# Check
number = actual_thing * 5
print(number)

# Exercise 2
other_thing = "11"
actual_other_thing = float(other_thing)
floating_number = actual_other_thing * 6
print(floating_number)

# Exercise 3
str_obj = "I like Frozen"
int_obj = 1
print(str_obj + str(int_obj))

# Exercise 4
input1 = input("Give me a number ")
input2 = input("Give me another number ")
product = float(input1) * float(input2)
print("The product of " + input1 + " and " + input2 + " is " + str(product))
