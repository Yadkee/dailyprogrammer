#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
from itertools import cycle
from operator import add, sub
from string import ascii_lowercase as ABC
p = ABC.index  # Position of a character in the abecedary
l = len(ABC)  # Length of the abecedary


def vigenere(key, data, op=add):  # Cipher with add, decipher with sub
    return "".join(ABC[op(p(i), p(j)) % l] for i, j in zip(data, cycle(key)))

print(vigenere(*"snitch thepackagehasbeendelivered".split()))
print(vigenere(*"bond theredfoxtrotsquietlyatmidnight".split()))
print(vigenere(*"train murderontheorientexpress".split()))
print(vigenere(*"garden themolessnuckintothegardenlastnight".split()))
print(vigenere(*"cloak klatrgafedvtssdwywcyty".split(), op=sub))
print(vigenere(*"python pjphmfamhrcaifxifvvfmzwqtmyswst".split(), op=sub))
print(vigenere(*"moore rcfpsgfspiecbcc".split(), op=sub))
