from modules.utils.fields import Phone, Email, Address, Birthday
from modules.utils.messages import *


def input_with_validation(
    prompt, validator, error_message, allow_empty=True, cancel_on_empty=False
):
    """
    Helper function for input with validation
    Допоміжна функція для введення з валідацією

    Args:
        prompt (str): Input prompt / Запрошення до введення
        validator (callable): Validation function / Функція валідації
        error_message (str): Error message / Повідомлення про помилку
        allow_empty (bool): Allow empty input / Дозволити пусте введення
        cancel_on_empty (bool): Cancel operation on empty input / Скасувати операцію при пустому введенні

    Returns:
        str or None: Validated input or None / Перевірене введення або None
        False: If operation was cancelled / Якщо операція була скасована
    """
    while True:
        value = input(prompt).strip()

        # Handle empty input
        if not value:
            if cancel_on_empty:
                return False  # Cancel operation
            if allow_empty:
                return None  # Skip field
            print(INVALID_NAME)
            continue

        # Validate non-empty input
        if validator(value):
            return value
        print(error_message)


def add_contact_interactive(assistant):
    """
    Interactive contact addition
    Інтерактивне додавання контакту
    """
    print(f"\n{ADDING_CONTACT}")

    # Name input / Введення імені
    while True:
        name = input(ENTER_NAME).strip()
        if not name:
            print(CANCELED_MESSAGE)
            return
        if assistant.contacts.find_contact_by_name(name):
            print(CONTACT_EXISTS)
            continue
        break

    # Other fields input / Введення інших полів
    phone = input_with_validation(ENTER_PHONE, Phone.validate, INVALID_PHONE)
    email = input_with_validation(ENTER_EMAIL, Email.validate, INVALID_EMAIL)
    address = input_with_validation(ENTER_ADDRESS, Address.validate, INVALID_ADDRESS)
    birthday = input_with_validation(ENTER_BIRTHDAY, Birthday.validate, INVALID_DATE)

    # Add contact
    result = assistant.add_contact(name, address, phone, email, birthday)
    if result or isinstance(result, bool):  # Added successfully or skipped some fields
        print(CONTACT_ADDED)


def edit_contact_interactive(assistant):
    """
    Interactive contact editing
    Інтерактивне редагування контакту
    """
    print(f"\n{EDITING_CONTACT}")

    # Get contact name / Отримання імені контакту
    name = input(ENTER_NAME).strip()
    if not name:
        print(CANCELED_MESSAGE)
        return

    contact = assistant.contacts.find_contact(name)
    if not contact:
        print(CONTACT_NOT_FOUND)
        return

    print(f"\nCurrent contact info:\n{contact}")
    print(
        "\nEnter new values (press Enter to keep current value, press Enter twice to cancel)"
    )

    # Edit fields / Редагування полів
    phone = input_with_validation(
        ENTER_PHONE, Phone.validate, INVALID_PHONE, cancel_on_empty=True
    )
    if phone is False:
        return

    email = input_with_validation(
        ENTER_EMAIL, Email.validate, INVALID_EMAIL, cancel_on_empty=True
    )
    if email is False:
        return

    address = input_with_validation(
        ENTER_ADDRESS, Address.validate, INVALID_ADDRESS, cancel_on_empty=True
    )
    if address is False:
        return

    birthday = input_with_validation(
        ENTER_BIRTHDAY, Birthday.validate, INVALID_DATE, cancel_on_empty=True
    )
    if birthday is False:
        return

    if assistant.contacts.update_contact(name, address, phone, email, birthday):
        print(CONTACT_UPDATED)
    else:
        print("Failed to update contact")


def delete_contact_interactive(assistant):
    """
    Interactive contact deletion
    Інтерактивне видалення контакту
    """
    print(f"\n{DELETING_CONTACT}")

    name = input(ENTER_NAME).strip()
    if not name:
        print(CANCELED_MESSAGE)
        return

    contact = assistant.contacts.find_contact(name)
    if not contact:
        print(CONTACT_NOT_FOUND)
        return

    print(f"\nFound contact:\n{contact}")
    confirm = input(CONFIRM_DELETE).lower().strip()

    if confirm == "y":
        if assistant.contacts.delete_contact(name):
            print(CONTACT_DELETED)
        else:
            print("Failed to delete contact")
    else:
        print(CANCELED_MESSAGE)


def show_search_results(matches):
    """
    Shows search results in a formatted way
    Показує результати пошуку у форматованому вигляді
    Args:
        matches (list): List of found contacts / Список знайдених контактів
    """
    if matches:
        print(f"\nFound {len(matches)} contact(s):")
        for i, contact in enumerate(matches, 1):
            print(f"{i}. {contact}")
    else:
        print(CONTACT_NOT_FOUND)


def search_contacts_interactive(assistant):
    """
    Interactive contact search
    Інтерактивний пошук контактів
    """
    print(f"\n{SEARCHING_CONTACTS}")
    print("Available search criteria:")
    print("1. By name")
    print("2. By phone")
    print("3. By email")

    choice = input(ENTER_SEARCH_CRITERIA).strip()
    if not choice:
        print(CANCELED_MESSAGE)
        return

    if choice == "1":
        name = input("Enter full or partial name: ").strip()
        if not name:
            print(CANCELED_MESSAGE)
            return
        matches = assistant.contacts.find_contacts(name)

    elif choice == "2":
        phone = input("Enter full or partial phone number: ").strip()
        if not phone:
            print(CANCELED_MESSAGE)
            return
        matches = assistant.contacts.find_by_phone(phone)

    elif choice == "3":
        email = input("Enter full or partial email: ").strip()
        if not email:
            print(CANCELED_MESSAGE)
            return
        matches = assistant.contacts.find_by_email(email)

    else:
        print(INVALID_CHOICE)
        return

    show_search_results(matches)


def show_birthdays_interactive(assistant):
    """
    Interactive birthday reminder
    Інтерактивний показ днів народження
    """
    print("\nBirthday reminder")

    days = input("Enter number of days to check (press Enter to cancel): ").strip()
    if not days:
        print(CANCELED_MESSAGE)
        return

    if not days.isdigit():
        print("Please enter a valid number")
        return

    print(NOT_IMPLEMENTED_MESSAGE.format("Birthday reminder"))
