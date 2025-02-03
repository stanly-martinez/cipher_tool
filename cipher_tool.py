from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

# Función para generar una clave AES de 256 bits
def generate_aes_key():
    return get_random_bytes(32)  # AES 256-bit key

# Función para cifrar un mensaje
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Cifrado CBC
    # Asegurarse de que el mensaje tenga longitud múltiplo de 16
    padded_message = message + (16 - len(message) % 16) * ' '
    ciphertext = cipher.encrypt(padded_message.encode())
    # Retorna el IV (Initialization Vector) y el mensaje cifrado, ambos codificados en base64
    return base64.b64encode(cipher.iv + ciphertext).decode()

# Función para descifrar un mensaje
def decrypt_message(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext).decode().strip()
    return decrypted_message

# Función para cifrar un archivo
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = data + (16 - len(data) % 16) * b' '  # Rellenar para múltiplo de 16
    ciphertext = cipher.encrypt(padded_data)
    with open(f"{file_path}.enc", 'wb') as f:
        f.write(cipher.iv + ciphertext)  # Escribir IV + mensaje cifrado

# Función para descifrar un archivo
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext).strip()
    with open(f"{file_path}.dec", 'wb') as f:
        f.write(decrypted_data)  # Escribir archivo descifrado

def cipher_tool():
    print("Generando clave AES de 256 bits...")
    key = generate_aes_key()  # Genera una nueva clave AES

    while True:
        print("\n--- Menú de Cifrado ---")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Cifrar archivo")
        print("4. Descifrar archivo")
        print("5. Salir")
        
        choice = input("Selecciona una opción (1-5): ")
        
        if choice == "1":
            message = input("Escribe el mensaje para cifrar: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Mensaje cifrado: {encrypted_message}")
        elif choice == "2":
            encrypted_message = input("Escribe el mensaje cifrado: ")
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Mensaje descifrado: {decrypted_message}")
        elif choice == "3":
            file_path = input("Ingresa la ruta del archivo a cifrar (ej. archivo.txt): ")
            if os.path.exists(file_path):
                encrypt_file(file_path, key)
                print(f"Archivo cifrado guardado como {file_path}.enc")
            else:
                print("El archivo no existe.")
        elif choice == "4":
            file_path = input("Ingresa la ruta del archivo a descifrar (ej. archivo.txt.enc): ")
            if os.path.exists(file_path):
                decrypt_file(file_path, key)
                print(f"Archivo descifrado guardado como {file_path}.dec")
            else:
                print("El archivo no existe.")
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    cipher_tool()
