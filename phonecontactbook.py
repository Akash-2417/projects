import time

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ").strip().capitalize()
    phone = input("Enter phone number: ").strip()
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name} - {phone}")
        print()

# Function to search and call a contact
def call_contact():
    name = input("Enter name to call: ").strip().capitalize()
    if name in contacts:
        print(f"\n📞 Calling {name} at {contacts[name]}...")
        for i in range(3):
            print(".", end='', flush=True)
            time.sleep(1)
        print(f"\n✅ Call connected to {name}!\n")
    else:
        print("❌ Contact not found.")

# Main menu
def menu():
    while True:
        print("=== Phone Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Call Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            call_contact()
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the contact book
menu()
