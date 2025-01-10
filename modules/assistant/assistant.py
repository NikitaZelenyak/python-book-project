from modules.contacts.contact_manager import ContactManager
from modules.notes.note_manager import NoteManager
from colorama import Fore, Style, init


class PersonalAssistant:
    def __init__(self):
        self.contacts = ContactManager()
        self.notes = NoteManager()
        self.commands = {
            "add": "Add a new note",
            "all": "View all notes",
            "edit": "Edit an existing note",
            "delete": "Delete a note",
            "search": "Search for notes by text",
            "search_note": "Search notes by text",
            "edit_tags": "Edit tags of a note",
            "search_by_tag": "Search notes by a specific tag",
            "filter_tag": "Filter notes by tag",
            "sort_by_tags": "Sort notes by tags",
        }

    def add_contact(self, name, address, phone, email, birthday):
        """
        Add a new contact using ContactManager
        Додайте новий контакт за допомогою ContactManager
        """
        self.contacts.add_contact(name, address, phone, email, birthday)

    def display_commands(self):
        print(f"{Fore.GREEN}ℹ️ Available commands:")
        for command, description in self.commands.items():
            print(f"{Fore.CYAN}{command}: {description}")

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

    def search_note_by_text(self):
        search_text = input("Enter text to search in notes: ")
        results = self.notes.search_note_by_text(search_text)
        if results:
            print("Found notes:")
            for note in results:
                print(note)
        else:
            print("No notes found containing the given text.")

    def edit_note_tags(self):
        note_id = input("Enter note ID: ")
        new_tags = input("Enter new tags (comma separated): ").split(",")
        self.notes.edit_note_tags(note_id, new_tags)
        print("Tags updated successfully!")

    def search_notes_by_tag(self):
        tag = input("Enter tag to search: ")
        results = self.notes.search_by_tag(tag)
        if results:
            print("\nNotes with tag:", tag)
            for note in results:
                print(note)
        else:
            print("No notes found with this tag.")

    def filter_notes_by_tag(self):
        tag = input("Enter tag to filter notes: ")
        results = self.notes.filter_notes_by_tag(tag)
        if results:
            print("Notes with tag '{}' found:".format(tag))
            for note in results:
                print(note)
        else:
            print("No notes found with the tag '{}'.".format(tag))

    def sort_notes_by_tags(self):
        sorted_notes = self.notes.sort_by_tags()
        print("\nNotes sorted by number of tags:")
        for note in sorted_notes:
            print(note)
