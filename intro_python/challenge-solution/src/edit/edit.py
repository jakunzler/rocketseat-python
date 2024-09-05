"""
Implementation of the functionality to edit the contacts.
"""

def edit_contact(contacts: list, name: str, phone: str, email: str, is_favorite: bool):
    """
    Edit a contact from the list of contacts.

    Parameters:
    contacts (list): List of contacts.
    name (str): Name of the contact to be edited.
    phone (str): New phone number of the contact.
    email (str): New email of the contact.
    is_favorite (bool): Whether the contact is a favorite or not.
    """
    
    try:
        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = phone if phone else contact["phone"]
                contact["email"] = email if email else contact["email"]
                contact["favorite"] = is_favorite if is_favorite else contact["favorite"]
                break
        else:
            raise ValueError("Contact not found.")
    except ValueError as error:
        print(f"Error: {error}")
        return
    else:
        print("Contact successfully edited!")
    finally:
        pass