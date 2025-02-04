# Cipher Tool

The **Cipher Tool** is a Python-based utility that allows users to encrypt and decrypt both messages and text files using AES-256 encryption. It utilizes the AES algorithm in CBC (Cipher Block Chaining) mode for secure encryption and decryption.

## Features
- **Encrypt Message**: Encrypt a plain text message using AES-256 encryption.
- **Decrypt Message**: Decrypt an encrypted message back to its original form.
- **Encrypt File**: Encrypt a text file with AES-256 and save the encrypted version.
- **Decrypt File**: Decrypt an encrypted file back to its original content.
- **Key Generation**: Automatically generates a 256-bit AES key for encryption/decryption.

## How It Works
1. **Key Generation**: The tool generates a 256-bit AES key upon startup, which is used for all encryption and decryption operations.
2. **Encryption/Decryption Modes**:
   - **Message Encryption/Decryption**: Text messages are padded to ensure their length is a multiple of 16 bytes (required for AES CBC mode).
   - **File Encryption/Decryption**: Files are read, padded to a multiple of 16 bytes, and then encrypted or decrypted accordingly.

3. **AES-CBC Mode**: The AES cipher is used in CBC mode, which requires an Initialization Vector (IV) for each encryption. The IV is generated randomly and stored alongside the ciphertext for decryption.

## Installation

### Dependencies
This project requires the **pycryptodome** library for AES encryption. To install the required dependencies, run the following command:
```bash
pip install pycryptodome 
```
or 

```bash
pip install pycryptodome --break-system-packages
```
### Usage

Once the dependencies are installed, you can run the `cipher_tool.py` file, and it will prompt you with a menu of options:

### Main Menu
```plaintext
--- Encryption Menu ---
1. Encrypt message
2. Decrypt message
3. Encrypt file
4. Decrypt file
5. Exit
Select an option (1-5):
```

### Options Explained:
1. **Encrypt Message**: Enter a message, and the tool will encrypt it using AES-256.
   - Example:
     ```plaintext
     Enter the message to encrypt: Hello, this is a secret!
     Encrypted message: <encrypted_base64_message>
     ```

2. **Decrypt Message**: Enter the encrypted message (in base64 format) and decrypt it back to the original message.
   - Example:
     ```plaintext
     Enter the encrypted message: <encrypted_base64_message>
     Decrypted message: Hello, this is a secret!
     ```

3. **Encrypt File**: Enter the file path (e.g., `file.txt`), and the tool will encrypt the file, saving it with a `.enc` extension.
   - Example:
     ```plaintext
     Enter the path of the file to encrypt: file.txt
     Encrypted file saved as file.txt.enc
     ```

4. **Decrypt File**: Enter the encrypted file path (e.g., `file.txt.enc`), and the tool will decrypt it, saving the result with a `.dec` extension.
   - Example:
     ```plaintext
     Enter the path of the file to decrypt: file.txt.enc
     Decrypted file saved as file.txt.dec
     ```

5. **Exit**: Exit the program.

### Example Output

#### Encrypt Message
```plaintext
--- Encryption Menu ---
1. Encrypt message
...
Select an option (1-5): 1
Enter the message to encrypt: Secret message!
Encrypted message: U2FsdGVkX1+yt88nM0VnVGBPCg== 
```

#### Decrypt Message
```plaintext
--- Encryption Menu ---
2. Decrypt message
...
Select an option (1-5): 2
Enter the encrypted message: U2FsdGVkX1+yt88nM0VnVGBPCg==
Decrypted message: Secret message!
```

#### Encrypt File
```plaintext
--- Encryption Menu ---
3. Encrypt file
...
Select an option (1-5): 3
Enter the path of the file to encrypt: example.txt
Encrypted file saved as example.txt.enc
```

#### Decrypt File
```plaintext
--- Encryption Menu ---
4. Decrypt file
...
Select an option (1-5): 4
Enter the path of the file to decrypt: example.txt.enc
Decrypted file saved as example.txt.dec
```

## Contributing
Feel free to fork the repository, enhance the functionality, and submit a pull request.

## License
This project is open-source and available for modification and distribution.
