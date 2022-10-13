# doing this because giselle wrote some self-referencing function in R
# but she wrote the function name in the function declaration
import numpy as np

x = 4
y = 9

def range_sum_proper(a, b):
#	a = int(input("first integer\n"))
#	b = int(input("second integer\n"))
	print(f"first integer received is {a}")
	print(f"second integer received is {b}")
	out = 0
	for i in range(a, b+1):
#		print(i) #debug
		out = out + i
#		print(out) #debug
	print(f"sum is {out}")

range_sum_proper(x, y)

#giselles code in R
"""
input <- readLines('stdin')
x <- as.integer(input[1])
y <- as.integer(input[2])
#define the function
rangeSum <- function(x,y) {
    for (x in x:y) {
        rangeSum(x,y)
    }
    result <- x+y
}
rangeSum(42, 64)
print(result)
"""

def range_sum_test(a, b):
	print(f"1st int is {a} and 2nd int is {b}\n")
	# in python3, range() is an iterator, form a list with list(range(n, m))
	for a in range(a, b):
		range_sum_test(a,b)
	result = a + b

#range_sum_test(x, y)
#print(result)
