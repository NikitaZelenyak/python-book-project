from modules.core.utils.file_manager import load_from_file, save_to_file
from modules.notes.note import Note

NOTES_FILE = "data/notes.json"

class NoteManager:
   def __init__(self):
      self.notes = [Note.from_dict(note) for note in load_from_file(NOTES_FILE) or []]

   def add_note(self, text, tags=None):
      note = Note(text, tags)
      self.notes.append(note)
      self._save_notes()

   def _save_notes(self):
      save_to_file(NOTES_FILE, [note.to_dict() for note in self.notes])

   def edit_note(self, note_id : str, new_text: str):
      for note in self.notes:
         if note.id.value == note_id:
            note.edit_text(new_text)
            self._save_notes()
            break

   def delete_note(self, note_id : str):
      self.notes = [note for note in self.notes if note.id != note_id]
      self._save_notes()

    def search_note_by_text(self, search_text: str):
        return [note for note in self.notes if search_text in note.text]

    def edit_note_tags(self, note_id: str, new_tags: list):
        for note in self.notes:
            if note.id.value == note_id:
                note.edit_tags(new_tags)
                self._save_notes()
                break

    def search_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]

    def filter_notes_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]

    def sort_by_tags(self):
        return sorted(self.notes, key=lambda note: len(note.tags), reverse=True)
     