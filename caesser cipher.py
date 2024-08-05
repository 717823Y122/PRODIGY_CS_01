def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            shift = key % 26
            if letter.isupper():
                ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(letter) + shift - 97) % 26 + 97)
        else:
            ciphertext += letter
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            shift = key % 26
            if letter.isupper():
                plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(letter) - shift - 97) % 26 + 97)
        else:
            plaintext += letter
    return plaintext
def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d/quit): ").lower()
        if choice == 'quit':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'quit' to exit.")
            continue
        text = input("Enter the text: ")
        key = int(input("Enter the key (number): "))
        if choice == 'e':
            result = encrypt(text, key)
            print(f"Encrypted text: {result}")
        elif choice == 'd':
            result = decrypt(text, key)
            print(f"Decrypted text: {result}")
if __name__ == "__main__":
    main()
