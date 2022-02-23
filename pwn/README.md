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









