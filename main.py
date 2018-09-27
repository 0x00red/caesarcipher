#!/usr/bin/env python3
import sys
ls = "abcdefghijklmnopqrstuvwxyz" #string of characters
punct = "\"'.,!?;:" ##punctuation is skipped
dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} #dictionary of letter to index pairing
input = raw_input ##hack-ish fix since shit wasn't working

##functions and shit

def encrypt(instring, shift, ls, dict, punct): #takes input text, shift, and a list and dictionary(for language support)
	instring = instring.split()
	out = ""
	for word in instring:
		for letter in word:
			if letter in punct:
				out = out + letter
				continue
			out = out + ls[(dict[letter] + shift) % len(ls)]
		out = out + " "
	return out[:-1]


def decrypt(cipher, shift, ls, dict, punct): #takes cipher, shift, list and dict(lang support) to decipher
	cipher = cipher.split()
	out = ""
	for word in cipher:
		for letter in word:
			if letter in punct:
				out = out + letter
				continue
			out = out + ls[(dict[letter] - shift) % len(ls)]
		out = out + " "
	return out[:-1]


##start program

while(1): ##makes sure the user selects a valid option
	print("[E]ncrypt or [D]ecrypt? ")
	eord = input()
	if len(eord) == 0:
		continue
	eord = eord.lower()
	if eord[0] == "e":
		break
	elif eord[0] == "d":
		break
	else:
		continue

##takes input and cipher key
print("Input text: ")
instring = input()
instring = instring.lower()
print("Input shift: ")
shift = input()
try:
	shift = int(shift)
except:
	print("Shift must be an integer.")
	sys.exit(0)

##does encryption or decryption and posts output
if eord[0] == "e":
	try:
		print(encrypt(instring, shift, ls, dict, punct))
	except:
		print("Only alphabetical characters and whitespace allowed.")
elif eord[0] == "d":
	try:
		print(decrypt(instring, shift, ls, dict, punct))
	except:
		print("Only alphabetical characters and whitespace allowed.")
