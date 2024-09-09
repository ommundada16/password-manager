import json
import os
from utils import print_red_text
from delete_password import delete_password
from reveal_password import reveal_password
from update_password import update_password
from load_master_password import load_master_password
from add_password import add_password
from view_password import view_passwords



if __name__ == "__main__":
    key = load_master_password()
    
    if not os.path.exists('passwords.json'):
        with open('passwords.json', 'w') as f:
            json.dump([], f)

    while True: 
        print("\nPassword Manager")
        print("1. Add a password")
        print("2. View passwords")
        print("3. Reveal password")
        print("4. Delete a password")
        print("5. Update a password")
        print("6. Exit")  

        choice = input("Enter your choice: ")

        if choice == '1':
            add_password(key)
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            user_name = input("Enter user name for whom you want to reveal: ")
            reveal_password(key, user_name)
        elif choice == '4':
            user_name = input("Enter user name for whom you want to delete password: ")
            delete_password(user_name)
        elif choice == '5':
            user_name = input("Enter user name for whom you want to update password: ")
            update_password(key, user_name)
        elif choice == '6':
            print("Exiting the Password Manager. Goodbye!")
            break 
        else:
            print_red_text("Invalid choice. Please try again.")
    