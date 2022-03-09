# Endian, 64-bit and 32-bit

p64() is for 64-bit, p32() for 32-bit, both in Little Endian.

p64() would usually be for 8 byte long addresses

For example, p64(win) would encode win in little endian, given win is in hex

p32() should be used for data types of size 4 bytes (like integers)

for example p32(0xdeadbeef) encodes 0xdeadbeef as a 4 byte little endian format

int(data, base) converts data into the specified base


# Addresses

To find the address, you usually have to use gdb

info function to find function addresses (for something like win)

or you can manually find it in the disassembly


# Stack pointer

win() has to run at rip, which is 8 bytes in front of rbp

rbp is easier to find so you can just +8

for win() you need p.interactive() otherwise it will close the connection

# checksec

when programs have a stack canary, there is a value placed on the stack that is checked before the function runs. if the value is not the same the program terminates.

if NX is enabled, when the application is loaded into the memory, it will not allow any segments to be both writeable or executable.

if PIE is not enabled, it tells the loader which virtual address to use, and the memory layout is quite static. 
when PIE is enabled, the memory is all scrambled so one needs to find the base address to calculate the offset from there.

# ret2libc

<https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc>

payload = padding + system + exit + "/bin/sh"
- exit is the return address for system()

find libc system function in gdb with `p system` and exit() with `p exit`. you want to force the program to call `system("/bin/sh")`

## find /bin/sh in libc
- find string in program with the string "/bin/sh", and libc contains that string
- inspect the memory layout of the program with `info proc map`, and identify where libc starts
- `strings -a -t x /lib/i386-linux-gnu/libc-2.27.so | grep "/bin/sh"` to find the offset of the string
- add the address of libc and "/bin/sh"
- check if the string is at the location with `x/s <addr>`

## find /bin/sh in the SHELL environment variable
- `x/s 500 $esp` to look at the stack and use eye power to find `"SHELL=/bin/sh"`
- the address + 6 will only give you "/bin/sh" (find the hexadecimal)
- 




