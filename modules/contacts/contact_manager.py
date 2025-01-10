from datetime import datetime, timedelta,date
from modules.core.utils.file_manager import load_from_file, save_to_file
from modules.core.constants.commands import CONTACTS_FILE
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
        print("\nSaving contacts to file:")
        data = []
        for contact in self.contacts:
            contact_dict = contact.to_dict()
            print(f"Saving contact: {contact_dict}")
            data.append(contact_dict)
        save_to_file(CONTACTS_FILE, data)
        print(f"Saved {len(data)} contacts")

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

    def get_all_contacts(self):
        """
        Returns all contacts sorted by name
        Повертає всі контакти, відсортовані за ім'ям
        Returns:
            list: List of contacts / Список контактів
        """
        return sorted(self.contacts, key=lambda x: str(x.name).lower())

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

    def find_by_phone(self, phone):
        """
        Finds contacts by partial phone number match
        Пошук контактів за частковим збігом номера телефону
        Args:
            phone (str): Phone number to find / Номер телефону для пошуку
        Returns:
            list: List of found contacts / Список знайдених контактів
        """
        matches = []
        search_phone = phone.lower()
        for contact in self.contacts:
            for p in contact.phones:
                if search_phone in str(p.value).lower():
                    matches.append(contact)
                    break  # Avoid duplicates if contact has multiple matching phones
        return sorted(matches, key=lambda x: str(x.name.value).lower())

    def find_by_email(self, email):
        """
        Finds contacts by partial email match
        Пошук контактів за частковим збігом email
        Args:
            email (str): Email to find / Email для пошуку
        Returns:
            list: List of found contacts / Список знайдених контактів
        """
        matches = []
        search_email = email.lower()
        for contact in self.contacts:
            if contact.email and search_email in contact.email.value.lower():
                matches.append(contact)
        return sorted(matches, key=lambda x: str(x.name.value).lower())

    def find_contacts(self, name):

        """
        Finds contacts by partial name match
        Пошук контактів за частковим збігом імені
        Args:
            name (str): Name to find / Ім'я для пошуку
        Returns:
            list: List of found contacts / Список знайдених контактів
        """
        matches = []
        search_name = name.lower()
        for contact in self.contacts:
            if search_name in contact.name.value.lower():
                matches.append(contact)
        return sorted(matches, key=lambda x: str(x.name.value).lower())
   
    def find_birthday_in_days(self, days_ahead):
        """
        Finds contacts whose birthday is within a given number of days from today.
        Пошук контактів, у яких день народження через задану кількість днів від поточної дати.

        Args:
            days_ahead (int): Number of days ahead to check for birthdays.
        
        Returns:
            list: List of contacts whose birthdays are within the specified days ahead.
        """
        today = datetime.now()
        upcoming_birthday_date = today + timedelta(days=days_ahead)
        upcoming_birthday_contacts = []

        for contact in self.contacts:
            if contact.birthday:
                # Get this year's birthday
                birthday_this_year = contact.birthday.replace(year=today.year)

                # Handle birthdays that have already passed this year
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                # Check if the birthday is within the given range
                if today <= birthday_this_year <= upcoming_birthday_date:
                    upcoming_birthday_contacts.append(contact)

        return upcoming_birthday_contacts