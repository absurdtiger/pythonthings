def check_palindrome(num, palindrome=True): # check if input is palindrome
       for i in range(int(len(num))//2):
               print(f"CHECKING PALINDROME: i is {i}, checking {num[i]} and {num[-i-1]}")
               if num[i]==num[-i-1]:
                       print(f"{num[i]} is palindromic")
                       continue
               else:
                       palindrome = False
                       print(f"{num[i]} and {num[-i-1]} is not a palindrome")
                       break
       if palindrome == False:
               print("i will get around to doing this")
       else:
               print("input is a palindrome. wow!")
               print(num)

def main():
	p = input("give number")
	check_palindrome(p)

while True:
	main()
	if input("Do you want the program to repeat? (Y)") == 'Y':
		print("repeating...")
		break

