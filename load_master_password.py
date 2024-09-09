import os
from getpass import getpass
from cryptography.fernet import Fernet

from utils import print_red_text, print_green_text, hash_password


# Hashing the master password for secure storage


# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Load or create a master password and ensure the key is valid
def load_master_password():
    if os.path.exists('master_password.txt'):
        # If master password exists, ask user to enter it for authentication
        while True:
            entered_password = getpass("Enter your master password: ")
            entered_password_hashed = hash_password(entered_password)
            with open('master_password.txt', 'r') as f:
                stored_password_hashed = f.read().strip()
            if entered_password_hashed == stored_password_hashed:
                print_green_text("Authentication successful.")
                break
            else:
                print_red_text("Incorrect master password. Try again.")
    else:
        # Create a master password if not already set
        print("Create a master password.")
        master_password = getpass("Enter a master password: ")
        print_red_text("Confirm your master password: ")
        confirm_password = getpass('')

        if master_password == confirm_password:
            with open('master_password.txt', 'w') as f:
                f.write(hash_password(master_password))  # Store hashed password
            print_green_text("Master password created successfully.")
        else:
            print_red_text("Passwords do not match. Please restart and try again.")
            exit(1)

    # Load the encryption key or create a new one
    if os.path.exists('master.key'):
        with open('master.key', 'rb') as f:
            key = f.read().strip()  # Ensure the key is properly loaded
            if len(key) != 44:
                raise ValueError("The key file is corrupted or invalid. Key must be 32 bytes and base64 encoded.")
            return key
    else:
        # Generate a new valid key
        key = generate_key()
        with open('master.key', 'wb') as f:
            f.write(key)  # Write the key correctly without extra characters
        return key
