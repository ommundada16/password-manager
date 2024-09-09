# Terminal-based Password Manager
This is a terminal-based password manager application built in Python. It allows users to securely manage passwords with encryption. Features include adding, viewing, updating, revealing, and deleting passwords. It also supports generating random strong passwords.

## Features
1. Add Password: Store account information with encrypted passwords.
2. View Saved Passwords: View account details after authentication with the master password.
3. Reveal Password: Reveal the stored password for an account after authentication.
4. Update Password: Update an existing password after verifying the current one.
5. Delete Password: Delete an account's password after verifying the current one.
6. Password Generation: Generate strong, random passwords.

## Setup Instructions

1. ### Install Dependencies
Ensure that Python is installed on your system. You can install the required dependencies using pip: 
> pip install -r requirements.txt

2. ### Set Up the Master Password
When you run the application for the first time, you will need to create a master password that secures all your other passwords.

This master password will be hashed and stored in the master_password.txt file.
Ensure that you remember this password, as you will need it to authenticate yourself in future sessions.

3.  ### Encrypting Passwords
The application uses AES encryption (cryptography.fernet) to securely store passwords in the passwords.json file. All passwords are encrypted before being stored and decrypted only when necessary.

  #### Encryption Keys:
  A master.key file will be automatically generated and stored when you run the program for the first time. This key is used to encrypt and decrypt the passwords.
  **Do NOT delete or modify this key, as it is essential for password decryption.**

4.  ### Running the Application
To run the password manager, use the following command:
> python main.py


## File Structure
```main.py```: The main application file that runs the password manager.
```add_password.py```: Contains the logic for adding a password.
```delete_password.py```: Contains the logic for deleting a password.
```update_password.py```: Contains the logic for updating a password.
```reveal_password.py```: Contains the logic for revealing a password.
```view_password.py```: Contains the logic for viewing stored passwords.
```passwords.json```: Stores the account information and encrypted passwords.
```master.key```: The encryption key used for encrypting and decrypting passwords.
```master_password.txt```: Stores the hashed master password.


