"""
Implementation of the functionality to save new contacts.
"""

def add_contact(contacts: list, name: str, phone: str, email: str, is_favorite: bool=False):
    """
    Add a new contact to the list of contacts.

    Parameters:
    contacts (list): List of contacts.
    name (str): Name of the contact.
    phone (str): Phone number of the contact.
    email (str): Email of the contact.
    is_favorite (bool): Whether the contact is a favorite or not (default: False).
    """
    
    try:
      for contact in contacts:
          # Verify if the contact already exists
          if contact["name"] == name:
              raise ValueError("Contact already exists.")
      
      # Add the new contact
      contacts.append({
          "name": name,
          "phone": phone,
          "email": email,
          "favorite": is_favorite
      })
    except ValueError as error:
      print(f"Error: {error}")
      return
    else:
      print("New contact successfully created!")
    finally:
      pass