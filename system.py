import re
import json

contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    identifier = input("Enter unique identifier (phone number or email): ")
    if identifier in contacts:
        print("Contact with this identifier already exists.")
        return
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")
    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact added successfully.")

def edit_contact():
    identifier = input("Enter unique identifier of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    additional_info = input("Enter new additional information (address, notes): ")
    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact updated successfully.")

def delete_contact():
    identifier = input("Enter unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    identifier = input("Enter unique identifier of the contact to search: ")
    if identifier in contacts:
        print(f"Details of contact {identifier}:")
        for key, value in contacts[identifier].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for identifier, details in contacts.items():
            print(f"\nIdentifier: {identifier}")
            for key, value in details.items():
                print(f"{key}: {value}")

def export_contacts():
    filename = input("Enter the filename to export contacts: ")
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file)
        print("Contacts exported successfully.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts():
    filename = input("Enter the filename to import contacts: ")
    try:
        with open(filename, 'r') as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
