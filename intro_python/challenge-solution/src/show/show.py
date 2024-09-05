"""
Implementation of the functionality to show the list of contacts.
"""

def show_contacts(contacts: list, contacts_group: str = ""):
    """
    Show all contacts in the list of contacts.

    Parameters:
    contacts (list): List of contacts.
    """
    
    if not contacts:
        print("No contacts found.")
        return
    
    if contacts_group == "only_favorites":
        print("\nFavorite contacts:")
        for contact in contacts:
            if contact["favorite"]:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
        print()
    elif contacts_group == "edit_contact":
      print("\nContacts:")
      for contact in contacts:
          print("\nName:", contact["name"])
          print("Phone:", contact["phone"])
          print("Email:", contact["email"])
          print("Favorite:", "Yes" if contact["favorite"] else "No")
      print()
    else:
      for contact in contacts:
          print("\nName:", contact["name"])
      print()