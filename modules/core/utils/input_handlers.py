from colorama import Fore
from modules.core.fields import Phone, Email, Address, Birthday
from modules.core.constants.messages import INVALID_EMAIL, INVALID_ADDRESS, INVALID_DATE


def handle_phones_input(prompt):
    """
    Handle phone numbers input with validation
    Обробка введення номерів телефонів з валідацією

    Args:
        prompt (str): Input prompt message / Повідомлення для введення

    Returns:
        list or None: List of valid phone numbers or None / Список валідних номерів або None
    """
    while True:
        phones_input = input(prompt).strip()
        if not phones_input:
            return None

        phone_list = [p.strip() for p in phones_input.split(",")]
        valid_phones = []
        invalid_phones = []

        for phone in phone_list:
            if Phone.validate(phone):
                valid_phones.append(phone)
            else:
                invalid_phones.append(phone)

        if invalid_phones:
            print(
                f"{Fore.RED}⚠️ Invalid phone number format: {', '.join(invalid_phones)}"
            )
            continue

        return valid_phones


def handle_email_input(prompt):
    """
    Handle email input with validation
    Обробка введення email з валідацією

    Args:
        prompt (str): Input prompt message / Повідомлення для введення

    Returns:
        str or None: Valid email or None / Валідний email або None
    """
    while True:
        email_input = input(prompt).strip()
        if not email_input:
            return None

        if Email.validate(email_input):
            return email_input
        print(f"{Fore.RED}⚠️ {INVALID_EMAIL}")


def handle_address_input(prompt):
    """
    Handle address input with validation
    Обробка введення адреси з валідацією

    Args:
        prompt (str): Input prompt message / Повідомлення для введення

    Returns:
        str or None: Valid address or None / Валідна адреса або None
    """
    while True:
        address_input = input(prompt).strip()
        if not address_input:
            return None

        if Address.validate(address_input):
            return address_input
        print(f"{Fore.RED}⚠️ {INVALID_ADDRESS}")


def handle_birthday_input(prompt):
    """
    Handle birthday input with validation
    Обробка введення дня народження з валідацією

    Args:
        prompt (str): Input prompt message / Повідомлення для введення

    Returns:
        str or None: Valid birthday date or None / Валідна дата народження або None
    """
    while True:
        birthday_input = input(prompt).strip()
        if not birthday_input:
            return None

        if Birthday.validate(birthday_input):
            return birthday_input
        print(f"{Fore.RED}⚠️ {INVALID_DATE}")
