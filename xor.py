#!/usr/bin/python

import sys

keyStream = sys.argv[1]
inputCiphertext = sys.argv[2]

#converting inputCiphertext to binary ciphertextstream
binaryCiphertext = (''.join(format(ord(x), 'b') for x in inputCiphertext))

#converting inputKey to binary keyStream
binaryKeyStream = (''.join(format(ord(x), 'b') for x in keyStream))

#print (binaryKeyStream,binaryCiphertext)

#
if (len(binaryCiphertext) <= len(binaryKeyStream)):
	index = 0
	for boolean in binaryCiphertext:
		binaryCleartext = int(binaryCiphertext[index]) ^ int(binaryKeyStream[index])
		index = index + 1
	
print binaryCleartext

