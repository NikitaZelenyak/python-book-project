from modules.contacts.contact_manager import ContactManager
from modules.notes.note_manager import NoteManager
class PersonalAssistant:
    def __init__(self):
        self.contacts = ContactManager()
        self.notes = NoteManager()
        

    def add_contact(self, name, address, phone, email, birthday):
        self.contacts.add_contact(name, address, phone, email, birthday)