import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)

#print(f"characters: {chars}")
#print(f"keys: {key}")

plain_text = input("Enter the message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

cipher_text = input("Enter the message to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Original message: {cipher_text}")
print(f"encrypted message: {plain_text}")