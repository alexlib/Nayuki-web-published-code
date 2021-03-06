# 
# This program shows how to call a cipher, and displays debugging information.
# Run with no arguments. For Python 2 and 3.
# 
# Copyright (c) 2015 Project Nayuki. (MIT License)
# https://www.nayuki.io/page/cryptographic-primitives-in-plain-python
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# - The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
# - The Software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and noninfringement. In no event shall the
#   authors or copyright holders be liable for any claim, damages or other
#   liability, whether in an action of contract, tort or otherwise, arising from,
#   out of or in connection with the Software or the use or other dealings in the
#   Software.
# 

import cryptocommon, aescipher


def main():
	message = "3243F6A8885A308D313198A2E0370734"
	key = "2B7E151628AED2A6ABF7158809CF4F3C"
	
	plaintextbytelist = cryptocommon.hexstr_to_bytelist(message)
	keybytelist = cryptocommon.hexstr_to_bytelist(key)
	ciphertextbytelist = aescipher.encrypt(plaintextbytelist, keybytelist, printdebug=True)
	ciphertexthexstr = cryptocommon.bytelist_to_hexstr(ciphertextbytelist)
	assert aescipher.decrypt(ciphertextbytelist, keybytelist) == plaintextbytelist
	
	print('Plaintext  (hex): {}'.format(message))
	print('Ciphertext (hex): {}'.format(ciphertexthexstr))
	print('Key        (hex): {}'.format(key))
	print("Plaintext  (bytelist): {}".format(plaintextbytelist))
	print("Ciphertext (bytelist): {}".format(ciphertextbytelist))
	print("Key        (bytelist): {}".format(keybytelist))


if __name__ == "__main__":
	main()
