from getpass import getpass
import json
from utils import decrypt_data, encrypt_data, print_green_text, print_red_text


def update_password(key, user_name):
    with open('passwords.json', 'r+') as f:
        data = json.load(f)
        account_found = False
        
        for entry in data:
            if entry['username'] == user_name:
                account_found = True
                existing_password = getpass("Enter the current password for the account: ")
                
                # Check if the entered password matches the existing password
                if decrypt_data(key, entry['password']) == existing_password:
                    new_password = getpass("Correct old password! Enter new password: ")
                    entry['password'] = encrypt_data(key, new_password).decode()
                    print_green_text(f"Password for {user_name} updated.")
                else:
                    print_red_text("Incorrect password. Update failed.")
                break
        
        # If account was not found
        if not account_found:
            print_red_text(f"Account {user_name} does not exist. Update failed.")
        
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()