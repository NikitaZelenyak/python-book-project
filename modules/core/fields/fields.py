from datetime import datetime
import re
from modules.core.constants.commands import DATE_FORMAT


class Field:
    """
    Base class for all fields
    Базовий клас для всіх полів
    """

    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        """
        Get field value / Отримати значення поля
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Set field value with validation / Встановити значення поля з валідацією
        """
        self._value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Class for storing contact name (required field)
    Клас для зберігання імені контакту (обов'язкове поле)
    """

    @Field.value.setter
    def value(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._value = value.strip()


class Phone(Field):
    """
    Class for storing phone number with validation
    Клас для зберігання номера телефону з валідацією
    """

    @Field.value.setter
    def value(self, value):
        if value and not self.validate(value):
            raise ValueError("Invalid phone number format")
        self._value = value

    @staticmethod
    def validate(phone):
        """
        Validates phone number format (10 digits)
        Перевіряє формат номера телефону (10 цифр)
        """
        return bool(re.match(r"^\d{10}$", phone))


class Email(Field):
    """
    Class for storing email with validation
    Клас для зберігання email з валідацією
    """

    @Field.value.setter
    def value(self, value):
        if value and not self.validate(value):
            raise ValueError("Invalid email format")
        self._value = value

    @staticmethod
    def validate(email):
        """
        Validates email format
        Перевіряє формат email
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))


class Birthday(Field):
    """
    Class for storing birthday with validation
    Клас для зберігання дня народження з валідацією
    """

    @Field.value.setter
    def value(self, value):
        if value:
            try:
                # Convert string to date
                date = datetime.strptime(value, DATE_FORMAT).date()

                # Validate date
                if not self.validate_date(date):
                    raise ValueError("Invalid date")

                self._value = date
            except ValueError:
                raise ValueError("Invalid date format")
        else:
            self._value = None

    @staticmethod
    def validate(value):
        """
        Validates date string format and logic
        Перевіряє формат та логіку дати
        """
        try:
            date = datetime.strptime(value, DATE_FORMAT).date()
            return Birthday.validate_date(date)
        except ValueError:
            return False

    @staticmethod
    def validate_date(date):
        """
        Validates date logic
        Перевіряє логіку дати
        """
        today = datetime.now().date()
        return date <= today and date.year >= 1900


class Address(Field):
    """
    Class for storing address with basic validation
    Клас для зберігання адреси з базовою валідацією
    """

    @Field.value.setter
    def value(self, value):
        if value and not self.validate(value):
            raise ValueError("Address is too short")
        self._value = value

    @staticmethod
    def validate(address):
        """
        Validates address (minimum length)
        Перевіряє адресу (мінімальна довжина)
        """
        return len(str(address).strip()) > 3
