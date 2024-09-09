from getpass import getpass
import json
from utils import authenticate, decrypt_data, print_green_text, print_red_text


# Reveal a password
def reveal_password(key, user_name):
    print_red_text("Enter your master password to confirm reveal data: ")
    entered_password = getpass('')
    auth = authenticate(entered_password)

    if auth:
        with open('passwords.json', 'r') as f:
            data = json.load(f)
            account_found = False
            for entry in data:
                if entry['username'] == user_name:
                    account_found = True
                    # Directly reveal the password without asking for the existing password
                    print_green_text(f"Password for {user_name}: {decrypt_data(key, entry['password'])}")
                    break
        
            # If account was not found, notify the user
            if not account_found:
                print_red_text(f"Account {user_name} does not exist. Reveal failed.")
    else:
        print_red_text('Authentication failed')