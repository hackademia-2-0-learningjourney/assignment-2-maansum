import json
import os

# Writing multiple records to a JSON file
def writefile():
    data = []
    # Check if the file already exists and has data
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    while True:
        name = input('Enter the name: ')
        email = input('Enter the email: ')
        password = input('Enter the password: ')
        contact = input('Enter the mobile number: ')

        # Create a dictionary for the new record
        record = {
            "name": name,
            "email": email,
            "password": password,
            "contact": contact
        }

        # Append the new record to the list
        data.append(record)

        # Ask if the user wants to continue adding records
        more = input('Do you want to add another record? (y/n): ')
        if more.lower() != 'y':
            break

    # Write all data back to the JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Data writing completed.")

# Reading and searching for a specific user in a JSON file
def readfile():
    if not os.path.exists('data.json'):
        print("The data file does not exist. Please create a file first by adding records.")
        return

    with open('data.json', 'r') as rd:
        try:
            data = json.load(rd)
        except json.JSONDecodeError:
            print("The data file is empty or corrupted.")
            return

        entered_email = input('Enter your email: ')
        entered_password = input('Enter your password: ')
        
        found = False
        for record in data:
            if entered_email == record['email'] and entered_password == record['password']:
                print(f'Access granted. The contact number for {record["name"]} is: {record["contact"]}')
                found = True
                break

        if not found:
            print('Access denied. Email or password is incorrect.')

# Example of usage
if __name__ == "__main__":
    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            writefile()
        elif choice == '2':
            readfile()
        else:
            print("Invalid option, please choose 1 or 2.")
        
        more = input("Do you want to continue? (y/n): ")
        if more.lower() != 'y':
            print("Exiting the program.")
            break