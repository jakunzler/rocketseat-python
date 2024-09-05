"""
This script implements a simple contact management application.

Features:
- Add a new contact (name, phone, email, favorite).
- Remove an existing contact.
- Update contact information.
- List all registered contacts.

Contacts are stored in a dictionary, where the key is the contact name, 
and the values are sub-dictionaries containing the phone and email.

The program displays an interactive menu allowing the user to choose the desired actions.
The execution is controlled within a loop until the user decides to exit.

Developed following PEP 8 best practices.

Author: Jonas Augusto Kunzler

Creation date: 09/04/2024
Last update: XX/XX/XXXX
"""

from ..save import save
from ..show import show
from ..edit import edit
from ..delete import delete

contacts = []
while True:
    print("\nContact App Menu:")
    print("1. Save contact")
    print("2. Show contacts")
    print("3. Show favorite contacts")
    print("4. Edit contacts")
    print("5. Delete contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            contact_name = input("Enter the contact name: ").strip()
            contact_phone = input("Enter the contact phone: ").strip()
            contact_email = input("Enter the contact email: ").strip()
            contact_favorite = input("Is the contact a favorite? (y/n): ").strip()
            is_favorite = True if contact_favorite.lower() == "y" else False
            save.add_contact(contacts, contact_name, contact_phone, contact_email, is_favorite)
        
        case 2:
            show.show_contacts(contacts)
        
        case 3:
            show.show_contacts(contacts, "only_favorites")
            
        case 4:
            show.show_contacts(contacts, "edit_contact")
            contact_name = input("Enter the name of the contact you want to update: ")
            new_phone = input("Enter the new contact phone: ")
            new_email = input("Enter the new contact email: ")
            new_favorite = input("Is the contact a favorite? (y/n): ")
            new_favorite = True if new_favorite.lower() == "y" else False
            edit.edit_contact(contacts, contact_name, new_phone, new_email, new_favorite)
        
        case 5:
            show.show_contacts(contacts)
            contact_name = input("Enter the name of the contact you want to delete: ")
            delete.delete_contact(contacts, contact_name)
        
        case 6:
            break
        
        case _:
            print("Invalid choice. Please try again.")

print("See you!")
