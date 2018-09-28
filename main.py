#!/usr/bin/env python3
import sys
ls = "abcdefghijklmnopqrstuvwxyz" #string of characters
capls = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ##capital letters
capdict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
punct = "\"'.,!?;:-_+=*" ##punctuation is skipped
pdict = {"\"": 0, "'": 1, ".": 2, ",": 3, "!": 4, "?": 5, ";": 6, ":": 7, "-": 8, "_": 9, "+": 10, "=": 11, "*": 12} ##dictionary for punctuation
dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} #dictionary of letter to index pairing
numls = "1234567890" ##number list
numdict = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "0": 9} ## did it with a dict for compatibality 
input = raw_input ##hack-ish fix since shit wasn't working

##functions and shit

def encrypt(instring, shift, ls, dict, punct, pdict, numls, numdict, capls, capdict): #takes input text, shift, and a list and dictionary(for language support)
	instring = instring.split()
	out = ""
	for word in instring:
		for letter in word:
			if letter in punct:
				out = out + punct[(pdict[letter] + shift) % len(punct)]
				continue
			if letter in numls:
				out = out + numls[(numdict[letter] + shift) % len(numls)]
				continue
			if letter in capls:
				out = out + capls[(capdict[letter] + shift) % len(capls)]
				continue
			out = out + ls[(dict[letter] + shift) % len(ls)]
		out = out + " "
	return out[:-1]


def decrypt(cipher, shift, ls, dict, punct, pdict, numls, numdict): #takes cipher, shift, list and dict(lang support) to decipher
	cipher = cipher.split()
	out = ""
	for word in cipher:
		for letter in word:
			if letter in punct:
				out = out + punct[(pdict[letter] - shift) % len(punct)]
				continue
			if letter in numls:
				out = out + numls[(numdict[letter] - shift) % len(numls)]
				continue
			if letter in capls:
				out = out + capls[(capdict[letter] - shift) % len(capls)]
				continue
			out = out + ls[(dict[letter] - shift) % len(ls)]
		out = out + " "
	return out[:-1]


##start program
fopen = 0
while(1): ##makes sure the user selects a valid option
	if fopen == 0:
		print("[E]ncrypt, [D]ecrypt, or [F]ile? ")
	else:
		print("[E]ncrypt, [D]ecrypt, or [T]ext? ")
	eord = input()
	if len(eord) == 0:
		continue
	eord = eord.lower()
	if eord[0] == "e":
		break
	elif eord[0] == "d":
		break
	elif eord[0] == "f":
		fopen = 1
		continue
	elif eord[0] == "t":
		fopen = 0
		continue
	else:
		continue

##takes input and cipher key
if fopen == 0:
	print("Input text: ")
	instring = input()
else:
	print("File: ")
	file = input()
	try:
		f = open(file,"r")
		instring = f.read()
		f.close()
	except:
		print("Error opening " + file)
		sys.exit(0)
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
		print(encrypt(instring, shift, ls, dict, punct, pdict, numls, numdict, capls, capdict))
	except:
		print("Only alphabetical characters, punctuation, and whitespace allowed.")
elif eord[0] == "d":
	try:
		print(decrypt(instring, shift, ls, dict, punct, pdict, numls, numdict))
	except:
		print("Only alphabetical characters, punctuation, and whitespace allowed.")
