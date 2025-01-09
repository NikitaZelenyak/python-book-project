from modules.contacts.contact_manager import ContactManager
from modules.notes.note_manager import NoteManager
class PersonalAssistant:
    def __init__(self):
        self.contacts = ContactManager()
        self.notes = NoteManager()
        

    def add_contact(self, name, address, phone, email, birthday):
        self.contacts.add_contact(name, address, phone, email, birthday)

    def add_note(self):
        text = input("Enter note text: ")
        tags = input("Enter tags (comma separated): ").split(",")
        self.notes.add_note(text, tags)
    
    def edit_note(self):
        note_id = input("Enter note id: ")
        new_text = input("Enter new text: ")
        self.notes.edit_note(note_id, new_text)
        print(f"Note edited successfully. {note_id}")

    def delete_note(self):
        note_id = input("Enter note id: ")
        self.notes.delete_note(note_id)
        print(f"Note deleted successfully. {note_id}")

    def all_notes(self):
        for note in self.notes.notes:
            print(note)