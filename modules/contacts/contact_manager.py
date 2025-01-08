from modules.utils.load_from_file import load_from_file
from modules.utils.save_to_file import save_to_file
from modules.contacts.contact import Contact

CONTACTS_FILE = "data/contacts.json"


class ContactManager:
    """
    Class for managing contacts collection / Клас для управління колекцією контактів
    """

    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        """
        Loads contacts from file / Завантажує контакти з файлу
        """
        data = load_from_file(CONTACTS_FILE)
        if data:
            for contact_data in data:
                contact = Contact(contact_data["name"])
                # Restore phones / Відновлюємо телефони
                for phone in contact_data.get("phones", []):
                    contact.add_phone(phone)
                # Restore birthday if exists / Відновлюємо день народження якщо є
                if contact_data.get("birthday"):
                    contact.add_birthday(contact_data["birthday"])
                # Restore email if exists / Відновлюємо email якщо є
                if contact_data.get("email"):
                    contact.add_email(contact_data["email"])
                # Restore address if exists / Відновлюємо адресу якщо є
                if contact_data.get("address"):
                    contact.add_address(contact_data["address"])
                self.contacts.append(contact)

    def save_contacts(self):
        """
        Saves contacts to file / Зберігає контакти у файл
        """
        data = [contact.to_dict() for contact in self.contacts]
        save_to_file(CONTACTS_FILE, data)

    def add_contact(self, name, address=None, phone=None, email=None, birthday=None):
        """
        Adds a new contact / Додає новий контакт
        Args:
            name (str): Contact name / Ім'я контакту
            address (str, optional): Physical address / Фізична адреса
            phone (str, optional): Phone number / Номер телефону
            email (str, optional): Email address / Адреса електронної пошти
            birthday (str, optional): Birthday in DD.MM.YYYY format / День народження
        Returns:
            bool: Success status / Статус успішності
        """
        # Check if contact with this name already exists
        if self.find_contact(name):
            return False

        contact = Contact(name)

        if address:
            contact.add_address(address)
        if phone:
            contact.add_phone(phone)
        if email:
            contact.add_email(email)
        if birthday:
            contact.add_birthday(birthday)

        self.contacts.append(contact)
        self.save_contacts()
        return True

    def find_contact(self, name):
        """
        Finds contact by name / Шукає контакт за ім'ям
        Args:
            name (str): Contact name to find / Ім'я контакту для пошуку
        Returns:
            Contact or None: Found contact or None / Знайдений контакт або None
        """
        for contact in self.contacts:
            if str(contact.name) == name:
                return contact
        return None

    def delete_contact(self, name):
        """
        Deletes contact by name / Видаляє контакт за ім'ям
        Args:
            name (str): Contact name to delete / Ім'я контакту для видалення
        Returns:
            bool: Success status / Статус успішності
        """
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            return True
        return False

    def update_contact(self, name, address=None, phone=None, email=None, birthday=None):
        """
        Updates contact information / Оновлює інформацію контакту
        Args:
            name (str): Contact name / Ім'я контакту
            address (str, optional): New physical address / Нова фізична адреса
            phone (str, optional): New phone number / Новий номер телефону
            email (str, optional): New email address / Нова адреса електронної пошти
            birthday (str, optional): New birthday / Новий день народження
        Returns:
            bool: Success status / Статус успішності
        """
        contact = self.find_contact(name)
        if not contact:
            return False

        if address:
            contact.add_address(address)
        if phone:
            contact.add_phone(phone)
        if email:
            contact.add_email(email)
        if birthday:
            contact.add_birthday(birthday)

        self.save_contacts()
        return True

    def get_all_contacts(self):
        """
        Returns all contacts / Повертає всі контакти
        Returns:
            list: List of contacts / Список контактів
        """
        return self.contacts
