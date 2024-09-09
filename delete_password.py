# Delete a password
from getpass import getpass
import json
from utils import authenticate, decrypt_data, print_green_text, print_red_text


def delete_password(user_name):
    with open('passwords.json', 'r+') as f:
        data = json.load(f)
        account_found = False
        
        for entry in data:
            if entry['username'] == user_name:
                account_found = True
                print_red_text("Are you sure you want to delete? Enter master password to confirm:  ")
                entered_password = getpass('')
                auth = authenticate(entered_password)
                
                # Check if the entered password matches the existing password
                if auth:
                    updated_data = [entry for entry in data if entry['username'] != user_name]
                    f.seek(0)
                    json.dump(updated_data, f, indent=4)
                    f.truncate()
                    print_green_text(f"Password for {user_name} deleted.")
                else:
                    print_red_text("Incorrect password. Deletion failed.")
                break
        
        # If account was not found
        if not account_found:
            print_red_text(f"Account {user_name} does not exist. Deletion failed.")