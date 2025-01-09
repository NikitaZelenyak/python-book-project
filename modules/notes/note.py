from modules.core.fields.fields import Field
import uuid

class Note:
    def __init__(self, text, tags=None, note_id=None):
        self.id = Field(note_id if note_id else str(uuid.uuid4()))
        self.text = Field(text)
        self.tags = Field(tags if tags else [])

    def edit_text(self, new_text):
        self.text.value = new_text

    def __str__(self):
        return f"Note: {self.text.value}, Tags: {', '.join(self.tags.value)}"
    
    def to_dict(self):
        return {
            "id": self.id.value,
            "text": self.text.value,
            "tags": self.tags.value,
        }
    
    @staticmethod
    def from_dict(note_dict):
        return Note(note_dict["text"], note_dict["tags"], note_dict["id"])