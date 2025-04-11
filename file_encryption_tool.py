from cryptography.fernet import Fernet
import os

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[✔] Key generated and saved as 'secret.key'")

# Load the key from file
def load_key():
    if not os.path.exists("secret.key"):
        print("[!] No key found. Please make sure 'secret.key' is in the folder.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt the file
def encrypt_file(file_path):
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted)

    print(f"[✔] File '{file_path}' encrypted to '{file_path}.enc'")

# Decrypt the file
def decrypt_file(encrypted_path, output_path):
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)

    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("[!] Decryption failed. Wrong key?")
        return

    with open(output_path, "wb") as file:
        file.write(decrypted)

    print(f"[✔] File decrypted and saved as '{output_path}'")

# Main menu
def main():
    print("🔐 File Encryption Tool")
    print("1. Generate new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        file_path = input("Enter the file name to encrypt: ")
        encrypt_file(file_path)
    elif choice == "3":
        encrypted_path = input("Enter the encrypted file name (e.g. file.txt.enc): ")
        output_path = input("Enter the name for the decrypted output file (e.g. decrypted.txt): ")
        decrypt_file(encrypted_path, output_path)
    else:
        print("[!] Invalid option")

if __name__ == "__main__":
    main()
