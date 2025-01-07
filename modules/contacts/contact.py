
import uuid
from modules.utils.field import Field

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.id = str(uuid.uuid4())  # Unique identifier for the contact
        self.name = Field(name)
        self.address = Field(address)
        self.phone = Field(phone, validator=self.validate_phone)
        self.email = Field(email, validator=self.validate_email)
        self.birthday = Field(birthday)

    @staticmethod
    def validate_phone(phone):
        # Validate phone number
        return phone.isdigit() and len(phone) >= 10

    @staticmethod
    def validate_email(email):
        # Validate email format
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def to_dict(self):
        # Convert the contact to a dictionary for saving.
        return {
            "id": self.id,
            "name": str(self.name),
            "address": str(self.address),
            "phone": str(self.phone),
            "email": str(self.email),
            "birthday": str(self.birthday),
        }
