
from modules.utils.load_from_file import load_from_file
from modules.utils.save_to_file import save_to_file
from modules.contacts.contact import Contact
CONTACTS_FILE = "data/contacts.json"



class ContactManager:
    def __init__(self):
        self.contacts = load_from_file(CONTACTS_FILE) or []

    def add_contact(self, name, address, phone, email, birthday):
        # Add a new contact.
        try:
            contact = Contact(name, address, phone, email, birthday)
            self.contacts.append(contact.to_dict())
            self._save_contacts()
            print("Contact added successfully!")
        except ValueError as e:
            print(f"Error adding contact: {e}")

    def _save_contacts(self):
        # Save contacts to file.
        save_to_file(CONTACTS_FILE, self.contacts)
