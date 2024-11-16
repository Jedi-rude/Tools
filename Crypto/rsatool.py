import argparse
import math

# Extended Euclidean Algorithm to compute the greatest common divisor and modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Function to calculate the modular inverse of e modulo phi_n
def mod_inverse(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError(f"e and phi_n are not coprime, so no modular inverse exists.")
    else:
        return x % phi_n

# Compute Euler's Totient function for n = p * q
def compute_totient(p, q):
    return (p - 1) * (q - 1)

# RSA encryption function
def rsa_encrypt(plaintext, e, n):
    return pow(plaintext, e, n)

# RSA decryption function
def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Convert a string to an integer (for simplicity, using ASCII values)
def string_to_int(s):
    return int.from_bytes(s.encode(), 'big')

# Convert an integer back to a string (ASCII values)
def int_to_string(i):
    byte_length = (i.bit_length() + 7) // 8
    return i.to_bytes(byte_length, 'big').decode()

# Function to calculate the private key d
def calculate_private_key(p, q, e):
    # Step 1: Compute Euler's Totient function (phi(n))
    phi_n = compute_totient(p, q)
    print(f"phi(n) = {phi_n}")
    
    # Step 2: Check if e and phi(n) are coprime (i.e., gcd(e, phi_n) == 1)
    if math.gcd(e, phi_n) != 1:
        raise ValueError(f"e = {e} is not coprime with φ(n) = {phi_n}. Please choose a different e.")
    
    # Step 3: Calculate the modular inverse of e modulo phi(n)
    d = mod_inverse(e, phi_n)
    
    return d

# Main function to parse arguments and perform encryption or decryption
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt messages using RSA.")
    
    # Add arguments
    parser.add_argument('operation', choices=['encrypt', 'decrypt', 'expo'], 
                        help="Choose 'encrypt' to encrypt, 'decrypt' to decrypt, or 'expo' to calculate the private key exponent (d).")
    parser.add_argument('message', help="The message to encrypt or decrypt (or 'expo' requires p, q, and e).")
    parser.add_argument('-e', type=int, help="The public key exponent (e) for encryption or the private key exponent (d) for decryption.")
    parser.add_argument('-n', type=int, help="The modulus (n) used for encryption or decryption.")
    parser.add_argument('-d', type=int, help="The private key exponent (d) for decryption. Required for decryption.")
    parser.add_argument('-p', type=int, help="Prime factor p for calculating d (used for 'expo' operation).")
    parser.add_argument('-q', type=int, help="Prime factor q for calculating d (used for 'expo' operation).")

    args = parser.parse_args()
    
    if args.operation == 'encrypt':
        # Convert the message to an integer for encryption
        message_int = string_to_int(args.message)
        
        # Encrypt the message
        ciphertext = rsa_encrypt(message_int, args.e, args.n)
        
        # Output the encrypted message
        print(f"Encrypted message (ciphertext): {ciphertext}")
    
    elif args.operation == 'decrypt':
        # Check if private key exponent (d) is provided for decryption
        if args.d is None:
            print("Error: Private key exponent (d) is required for decryption.")
            return
        
        # Convert the ciphertext to integer if it's a string
        ciphertext_int = int(args.message)
        
        # Decrypt the ciphertext
        decrypted_message_int = rsa_decrypt(ciphertext_int, args.d, args.n)
        
        # Convert the decrypted integer back to a string
        decrypted_message = int_to_string(decrypted_message_int)
        
        # Output the decrypted message
        print(f"Decrypted message: {decrypted_message}")
    
    elif args.operation == 'expo':
        # Ensure that p, q, and e are provided
        if args.p is None or args.q is None or args.e is None:
            print("Error: Prime factors p, q, and public exponent e are required to calculate d.")
            return
        
        # Calculate the private exponent d
        try:
            d = calculate_private_key(args.p, args.q, args.e)
            print(f"Calculated private key exponent d: {d}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
