
import re
from utils import find_if_exists,print_red_text,encrypt_data,print_green_text
from getpass import getpass
import random
import string
import os
import json


# Generate random password
def generate_random_password(length=12, complexity="medium"):
    if complexity in ["high", "h"]:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity in  ["low","l"]:
        characters = string.ascii_lowercase 
    else:
        characters = string.ascii_letters + string.digits 

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_suggested_password():
    suggest_password = input("Should I suggest a password? (yes/no): ").strip().lower()

    if suggest_password in ['yes', 'y']:
        length = int(input("Enter desired password length: "))
        complexity = input("Select complexity (low, medium, high): ").strip().lower()
        generated_password = generate_random_password(length=length, complexity=complexity)
        print(f"Suggested password : {generated_password}")

        use_suggested = input("Do you want to use this suggested password? (yes/no): ").strip().lower()
        if use_suggested in ['yes', 'y']:
            return generated_password
    return getpass("Enter your own password: ")


# Function to validate email using regex
def is_valid_email(email):
    # Define a regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    return re.match(pattern, email)

#validate email
def get_email():
    while True:
        email = input("Enter email: ")
        if is_valid_email(email):
            return email
        else:
            print_red_text("Invalid email format. Please try again.")

# Function to save the password, now with email
def save_password(account, username, encrypted_password, email):
    if not os.path.exists('passwords.json'):
        with open('passwords.json', 'w') as f:
            json.dump([], f)

    with open('passwords.json', 'r+') as f:
        data = json.load(f)

        data.append({
            'account': account,
            'email': email,
            'username': username,
            'password': encrypted_password.decode(),
            
        })
        f.seek(0)
        json.dump(data, f, indent=4)

    print_green_text(f"Password for {username} added successfully!")

# Add a password
def add_password(key):
    account = input("Enter account name: ")

    # Get the email and validate it
    while True:
        email = get_email()
        
        if find_if_exists('email',email):
            print_red_text(f"Email '{email}' already used'. Please choose another email.")
        else:
            break


    while True:
        username = input("Enter username: ")
        if find_if_exists('username', username):
            print_red_text(f"Username '{username}' already exists'. Please choose another username.")
        else:
            break

    

    password = get_suggested_password()
    encrypted_password = encrypt_data(key, password)

    save_password(account, username, encrypted_password, email)