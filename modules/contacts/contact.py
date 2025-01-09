import uuid
from modules.core.fields import Name, Phone, Birthday, Email, Address
from modules.core.constants.commands import DATE_FORMAT


class Contact:
    """
    Class for storing contact information / Клас для зберігання інформації про контакт
    """

    def __init__(self, name, address=None, phone=None, email=None, birthday=None):
        self.id = str(uuid.uuid4())  # Unique identifier / Унікальний ідентифікатор
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)
        self.birthday = None
        if birthday:
            self.add_birthday(birthday)
        self.email = None
        if email:
            self.add_email(email)
        self.address = None
        if address:
            self.add_address(address)

    def add_phone(self, phone):
        """
        Adds a phone number / Додає номер телефону
        Args:
            phone (str): Phone number / Номер телефону
        Returns:
            bool: Success status / Статус успішності
        """
        phone_field = Phone(phone)
        if phone_field.value is None:
            return False
        if not self.find_phone(phone_field.value):
            self.phones.append(phone_field)
            return True
        return False

    def find_phone(self, phone):
        """
        Finds a phone number / Шукає номер телефону
        Args:
            phone (str): Phone number to find / Номер телефону для пошуку
        Returns:
            Phone object or None / Об'єкт Phone або None
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        """
        Adds a birthday / Додає день народження
        Args:
            birthday (str): Birthday in DD.MM.YYYY format / День народження у форматі ДД.ММ.РРРР
        Returns:
            bool: Success status / Статус успішності
        """
        if self.birthday is None:
            birthday_field = Birthday(birthday)
            print(birthday_field)
            if birthday_field.value is not None:
                self.birthday = birthday_field
                return True
        return False

    def add_email(self, email):
        """
        Adds an email / Додає email
        Args:
            email (str): Email address / Адреса електронної пошти
        Returns:
            bool: Success status / Статус успішності
        """
        if self.email is None:
            email_field = Email(email)
            if email_field.value is not None:
                self.email = email_field
                return True
        return False

    def add_address(self, address):
        """
        Adds an address / Додає адресу
        Args:
            address (str): Physical address / Фізична адреса
        Returns:
            bool: Success status / Статус успішності
        """
        if self.address is None:
            address_field = Address(address)
            if Address.validate(address):
                self.address = address_field
                return True
        return False

    def remove_phone(self, phone):
        """
        Removes a phone number / Видаляє номер телефону
        Args:
            phone (str): Phone number to remove / Номер телефону для видалення
        Returns:
            bool: Success status / Статус успішності
        """
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """
        Changes a phone number / Змінює номер телефону
        Args:
            old_phone (str): Old phone number / Старий номер телефону
            new_phone (str): New phone number / Новий номер телефону
        Returns:
            bool: Success status / Статус успішності
        """
        new_phone_field = Phone(new_phone)
        if new_phone_field.value is None:
            return False

        if self.remove_phone(old_phone):
            self.phones.append(new_phone_field)
            return True
        return False

    def to_dict(self):
        """
        Converts contact to dictionary / Конвертує контакт в словник
        Returns:
            dict: Contact data / Дані контакту
        """
        return {
            "id": self.id,
            "name": str(self.name),
            "phones": [str(p) for p in self.phones],
            "birthday": str(self.birthday.value) if self.birthday else None,
            "email": str(self.email) if self.email else None,
            "address": str(self.address) if self.address else None,
        }

    def __str__(self):
        """
        String representation of contact / Рядкове представлення контакту
        Returns:
            str: Contact info / Інформація про контакт
        """
        components = [f"Contact name: {self.name}"]

        if self.phones:
            phones = ", ".join(str(p) for p in self.phones)
            components.append(f"phones: {phones}")

        if self.birthday:
            date_str = self.birthday.value.strftime(DATE_FORMAT)
            components.append(f"birthday: {date_str}")

        if self.email:
            components.append(f"email: {self.email}")

        if self.address:
            components.append(f"address: {self.address}")

        return ", ".join(components)
