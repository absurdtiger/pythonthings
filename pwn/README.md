# All the information I organised here last time is gone. curse you inconsistent saving behaviour

## general pwn notes
GENERAL PAYLOAD: [buffer][addr of win() or syscall] 

### basic idea
- function that allows for buffer overflow (overwriting more data than it's supposed to)
- overwrite RIP
- control program and execution
- it's ROP if there are many gadgets
- it's libc if there is libc
- this should be double confirmed

### data formatting
- little endian is just the order in which the hex is presented and read
- p64() is for 64-bit
- p32() for 32-bit
- both p64() and p32() are in Little Endian
- p64() would usually be for 8 byte long addresses
- p32() should be used for data types of size 4 bytes (like integers)
- int(data, base) converts data into the specified base
- addresses can be declared as p64(0xdeadbeef) which would store it as 8-bit bytes
- non-hex strings must be converted into base 16 strings with int(b"string", 16) before being converted to 8-bit

### Addresses
gdb is useful
- `file [binary]` to select a file
- `pattern create 2000` to create de brujin sequence of 2000 digits long
- `r` to run binary
- `pattern search $rbp` to find rbp offset
  - if you can successfully find rbp in little-endian, rip is offset of rbp + 8
- alternatively `info frame` will show you rip and whether it is overwritten
  - there's not really an easy way to find the offset from the overwritten sequence but you can still try
- `info function` finds function addresses but it's a bit of a dump
  - most of pwn is not finding function addresses anyway unless libc
- in the event that gdb is annoying and won't give you the offset use a diff disassembler like IDA or binaryninja

## more about registers
**general purpose registers** are RAX, RBX, RCX, RDX, RDI, RSI, RBP, RSP, R8-15
**segments** are ES, CS, SS, DS, FS
**EFLAGS** are CF, PF, AF, ZF, SF,...
RIP: special _instruction pointer_ and is modified as a side-effect
RAX: accumulator
RBX: base
RCX: counter
RDX: data/general
RSI: source index
RDI: destination index
RBP: base pointer
RSP: stack pointer

### checksec
- stack canary checks if a value on the stack has remained constant. if the function is not the same the program terminates
- NX disallows segments from being both writeable or executable when loaded into memory
- PIE changes the virtual addresses of the program and stops it from being static
  - if PIE is enabled you need to find the base address and calculate the offset from there

### null-terminating strings
[1 NULL][buffer] <- compare with -> [1 NULL][unknown comparison]
buffer overflow is required to overwrite the second value in the strcmp\n
alternatively, \n
[NULL] <- compare with -> [NULL][unknown string]


## ROP
[buffer][ret][write "/bin/sh\x00" into memory][chain requirement for execve][syscall]

### rop chain to write /bin/sh into memory
- find a `mov qword ptr` gadget
- find a free space in the memory
  - CTRL+C to finish a program without entering any input
  - `vmmap` in gdb
  - `x/8x 0xaddress`
- change the registers in the gadget to reflect the location in the memory and "/bin/sh\x00"

### find /bin/sh in libc
- find string in program with the string "/bin/sh", and libc contains that string
- inspect the memory layout of the program with `info proc map`, and identify where libc starts
- `strings -a -t x /lib/i386-linux-gnu/libc-2.27.so | grep "/bin/sh"` to find the offset of the string
- add the address of libc and "/bin/sh"
- check if the string is at the location with `x/s <addr>`

### find /bin/sh in the SHELL environment variable (unreliable)
- `x/500s $rsp` or $esp to look at the stack and use eye power to find `"SHELL=/bin/sh"`
- the address + 6 will only give you "/bin/sh" (find the hexadecimal)

## libc
ugh
