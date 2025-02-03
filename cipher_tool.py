from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

# Function to generate a 256-bit AES key
def generate_aes_key():
    return get_random_bytes(32)  # AES 256-bit key

# Function to encrypt a message
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)  # CBC encryption
    # Ensure the message length is a multiple of 16
    padded_message = message + (16 - len(message) % 16) * ' '
    ciphertext = cipher.encrypt(padded_message.encode())
    # Return the IV (Initialization Vector) and the encrypted message, both base64 encoded
    return base64.b64encode(cipher.iv + ciphertext).decode()

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext).decode().strip()
    return decrypted_message

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = data + (16 - len(data) % 16) * b' '  # Pad to a multiple of 16
    ciphertext = cipher.encrypt(padded_data)
    with open(f"{file_path}.enc", 'wb') as f:
        f.write(cipher.iv + ciphertext)  # Write IV + encrypted data

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext).strip()
    with open(f"{file_path}.dec", 'wb') as f:
        f.write(decrypted_data)  # Write decrypted file

def cipher_tool():
    print("Generating 256-bit AES key...")
    key = generate_aes_key()  # Generate a new AES key

    while True:
        print("\n--- Encryption Menu ---")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Encrypt file")
        print("4. Decrypt file")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == "3":
            file_path = input("Enter the path of the file to encrypt (e.g., file.txt): ")
            if os.path.exists(file_path):
                encrypt_file(file_path, key)
                print(f"Encrypted file saved as {file_path}.enc")
            else:
                print("The file does not exist.")
        elif choice == "4":
            file_path = input("Enter the path of the file to decrypt (e.g., file.txt.enc): ")
            if os.path.exists(file_path):
                decrypt_file(file_path, key)
                print(f"Decrypted file saved as {file_path}.dec")
            else:
                print("The file does not exist.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    cipher_tool()
