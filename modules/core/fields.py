from datetime import datetime
import re


class Field:
    """
    Base class for all fields / Базовий клас для всіх полів
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Class for storing contact name (required field)
    Клас для зберігання імені контакту (обов'язкове поле)
    """

    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    """
    Class for storing phone number with validation
    Клас для зберігання номера телефону з валідацією
    """

    def __init__(self, value):
        self.value = None
        if self.validate(value):
            self.value = value

    @staticmethod
    def validate(phone):
        """
        Validates the phone number format
        Перевіряє формат номера телефону
        Args:
            phone (str): Phone number (10 digits)
        Returns:
            bool: True if valid, False if not
        """
        return bool(re.match(r"^\d{10}$", phone))


class Email(Field):
    """
    Class for storing email with validation
    Клас для зберігання email з валідацією
    """

    def __init__(self, value):
        self.value = None
        if self.validate(value):
            self.value = value

    @staticmethod
    def validate(email):
        """
        Validates the email format
        Перевіряє формат email
        Args:
            email (str): Email address
        Returns:
            bool: True if valid, False if not
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))


class Address(Field):
    """
    Class for storing address
    Клас для зберігання адреси
    """

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def validate(address):
        """
        Validates the address (minimum length)
        Перевіряє адресу (мінімальна довжина)
        Args:
            address (str): Physical address
        Returns:
            bool: True if valid, False if not
        """
        return len(str(address).strip()) > 3


class Birthday(Field):
    """
    Class for storing birthday with validation
    Клас для зберігання дня народження з валідацією
    """

    def __init__(self, value):
        self.value = None
        if self.validate(value):
            try:
                self.value = datetime.strptime(value, "%d.%m.%Y").date()
            except ValueError:
                pass

    @staticmethod
    def validate(value):
        """
        Validates the birthday format and logic
        Перевіряє формат та логіку дати народження
        Args:
            value (str): Date in format DD.MM.YYYY
        Returns:
            bool: True if valid, False if not
        """
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()

            # Check if date is not in future
            if date > datetime.now().date():
                return False

            # Check if year is not less than 1900
            if date.year < 1900:
                return False

            return True
        except ValueError:
            return False
