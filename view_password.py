import json
from utils import print_red_text

def formatted_data(data,seen_accounts):
    # Define a header with formatting
    header = "{:<10} {:<25} {:<15}".format("Name", "Email", "Username")

    # Print the header
    print(header)
    print("-" * len(header))  # Print a separator line

    # Loop through data and print each row with formatted columns
    for entry in data:
        username = entry.get('username', 'Unknown Username')
        if username not in seen_accounts:        
            seen_accounts.add(username)
            row = "{:<10} {:<25} {:<15}".format(entry["account"], entry["email"], entry["username"])
            print(row)

# View all passwords
def view_passwords():
    try:
        with open('passwords.json', 'r') as f:
            data = json.load(f)
            if len(data) == 0:
                print("No passwords found. Add Users!")
                return
            # Safely iterate through the data and ensure each entry has both account and username
            seen_accounts = set()  # To track and avoid duplicates
            formatted_data(data, seen_accounts)
                
    except (FileNotFoundError, json.JSONDecodeError):
        print_red_text("Error: Could not read passwords file. It may be empty or corrupted.")
