# Python 3 code to demonstrate the working of MD5 (string - hexadecimal)
# taken from https://www.geeksforgeeks.org/md5-hash-python/

import hashlib

# initializing string
str2hash = "examplestring"

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

#result.hexdigest is a string and can be sliced based on the index 
print(result.hexdigest[0:5]) 

#can also be compared to another string in an if statement
if result.hexdigest[0:5] == "00000" : 
	print("this hash is interesting!")
else :
	print("this hash is normal :(")




