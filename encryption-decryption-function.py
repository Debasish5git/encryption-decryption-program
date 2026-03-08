import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#encrypt
def encrypt():

    plain_text = input("Enter message to be encrypted: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Encrypted text is {cipher_text}")

#decrypt
def decrypt():
    
    cipher_text = input("Enter message to be decrypted: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"The decoded text is {plain_text}")

def main():

    is_running = True

    while is_running:

        print("\nEncryption-Decryption program")
        print("1.Encrypt message")
        print("2.Decrypt message")
        print("3.Exit program")

        choice = int(input("Enter the choice: "))

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            is_running = False
        else:
            print("Invalid Input!")


if __name__ == '__main__':
    main()