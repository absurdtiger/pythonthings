### 5.5 math functions and number functions ###

# round() to round a number to the nearest int
# a tie is a number that ends with 5
# python rounds ties to even
# specify the number of dp in round() with second arg
# round(n, p) where p is an integer
# abs() gives the positive number of an int or float
# pow() is different from ** because it accepts a third argument to take modulo as
# use .is_integer() on a float to check if it has a fractional component

# ex1
num1 = input("Enter a number: ")
num2 = round(float(num1), 2)
print(f"{num1} rounded to 2 decimal places is {num2}")

# ex2
num1 = input("Enter a number: ")
num2 = abs(float(num1))
print(f"The absolute value of {num1} is {num2}")

# ex3
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
difference = float(num1) - float(num2)
answer = difference.is_integer()
print(f"The difference between {num1} and {num2} is an integer? {answer}!")
