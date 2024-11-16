import argparse

# Function for encryption (Caesar Cipher)
def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            # Determine if character is upper or lower case
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-alphabetical characters remain unchanged
    return ''.join(encrypted_text)

# Function for decryption (Caesar Cipher)
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with a negative shift

# Main function to parse arguments and call encrypt or decrypt functions
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using Caesar Cipher.")
    
    # Adding arguments
    parser.add_argument('operation', choices=['encrypt', 'decrypt'], help="Choose 'encrypt' to encrypt or 'decrypt' to decrypt the message.")
    parser.add_argument('text', help="The text to encrypt or decrypt.")
    parser.add_argument('shift', type=int, help="The shift value (integer) for the Caesar Cipher.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    if args.operation == 'encrypt':
        result = encrypt(args.text, args.shift)
        print(f"Encrypted text: {result}")
    elif args.operation == 'decrypt':
        result = decrypt(args.text, args.shift)
        print(f"Decrypted text: {result}")

if __name__ == '__main__':
    main()
