from cryptography.fernet import Fernet
import os
import json
import hashlib


RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def print_red_text(message):
    print(f"{RED}{message}{RESET}")
    
def print_green_text(message):
    print(f"{GREEN}{message}{RESET}")

# Encrypt data
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())

# Decrypt data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_data).decode()

def find_if_exists(property,value):
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as f:
            data = json.load(f)

        for entry in data:
            if entry.get(property) == value:
                return True
    return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(key):
     entered_password_hashed = hash_password(key)
     with open('master_password.txt', 'r') as f:
                stored_password_hashed = f.read().strip()
     if entered_password_hashed == stored_password_hashed:
          return True
     else:
          return False
     