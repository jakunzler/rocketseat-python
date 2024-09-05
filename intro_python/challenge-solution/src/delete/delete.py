"""
Implementation of the functionality to delete a contact.
"""

def delete_contact(contacts: list, name: str):
    """
    Delete a contact from the list of contacts.

    Parameters:
    contacts (list): List of contacts.
    name (str): Name of the contact to be deleted.
    """
    
    try:
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                break
        else:
            raise ValueError("Contact not found.")
    except ValueError as error:
        print(f"Error: {error}")
        return
    else:
        print("Contact successfully deleted!")
    finally:
        pass