#!/usr/bin/python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

print "Running example AES CBC-mode block cipher"

BLOCKLEN = 16
# the blocks() function splits data string into space-speparated blocks

def blocks(data):
	split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]
	return ' '.join(split)
k = urandom(16)
print "k = %s" % hexa(k)

# pick a random Initialization Vector (IV)

iv = urandom(16)
print "iv = %s" % hexa(iv)

# pick an instance of AES in CBC-mode
aes = Cipher(algorithms.AES(k), modes.CBC(iv), backend=default_backend()).encryptor()

p = '\x00' * BLOCKLEN * 2
c = aes.update(p) + aes.finalize()

print "enc(%s) = %s" % (blocks(p), blocks(c))



