from modules.utils.load_from_file import load_from_file
from modules.utils.save_to_file import save_to_file
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