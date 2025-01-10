from modules.core.fields import Phone, Email, Address, Birthday
from modules.core.constants.messages import *
from modules.core.utils.input_manager import input_with_validation
from colorama import Fore, Style, init

def add_contact_interactive(assistant):
    """
    Interactive contact addition
    Інтерактивне додавання контакту
    """
    print(f"\n{Fore.GREEN}➕ {ADDING_CONTACT}")

    # Name input / Введення імені
    while True:
        name = input(f"{Fore.CYAN}{ENTER_NAME}").strip()
        if not name:
            print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
            return
        if assistant.contacts.find_contact(name):
            print(f"{Fore.RED}❌ {CONTACT_EXISTS}")
            continue
        break

    # Other fields input / Введення інших полів
    phone = input_with_validation(f"{Fore.CYAN}{ENTER_PHONE}", Phone.validate, f"{Fore.RED}⚠️ {INVALID_PHONE}")
    email = input_with_validation(f"{Fore.CYAN}{ENTER_EMAIL}", Email.validate, f"{Fore.RED}⚠️ {INVALID_EMAIL}")
    address = input_with_validation(f"{Fore.CYAN}{ENTER_ADDRESS}", Address.validate, f"{Fore.RED}⚠️ {INVALID_ADDRESS}")
    birthday = input_with_validation(f"{Fore.CYAN}{ENTER_BIRTHDAY}", Birthday.validate, f"{Fore.RED}⚠️ {INVALID_DATE}")

    result = assistant.add_contact(name, address, phone, email, birthday)
    if result or isinstance(result, bool):
        print(f"{Fore.GREEN}✅ {CONTACT_ADDED}")


def edit_contact_interactive(assistant):
    """
    Interactive contact editing
    Інтерактивне редагування контакту
    """
    print(f"\n{Fore.BLUE}✏️ {EDITING_CONTACT}")

    # Get contact name / Отримання імені контакту
    name = input(f"{Fore.CYAN}{ENTER_NAME}").strip()
    if not name:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
        return

    contact = assistant.contacts.find_contact(name)
    if not contact:
        print(f"{Fore.RED}❌ {CONTACT_NOT_FOUND}")
        return

    print(f"\n{Fore.YELLOW}ℹ️ Current contact info:\n{contact}")
    print("\nEnter new values (press Enter to keep current value)")

    # Edit fields / Редагування полів
    phone = input_with_validation(f"{Fore.CYAN}{ENTER_PHONE}", Phone.validate, f"{Fore.RED}⚠️ {INVALID_PHONE}")
    email = input_with_validation(f"{Fore.CYAN}{ENTER_EMAIL}", Email.validate, f"{Fore.RED}⚠️ {INVALID_EMAIL}")
    address = input_with_validation(f"{Fore.CYAN}{ENTER_ADDRESS}", Address.validate, f"{Fore.RED}⚠️ {INVALID_ADDRESS}")
    birthday = input_with_validation(f"{Fore.CYAN}{ENTER_BIRTHDAY}", Birthday.validate, f"{Fore.RED}⚠️ {INVALID_DATE}")

    if assistant.contacts.update_contact(name, address, phone, email, birthday):
        print(f"{Fore.GREEN}✅ {CONTACT_UPDATED}")
    else:
        print(f"{Fore.RED}❌ Failed to update contact")


def delete_contact_interactive(assistant):
    """
    Interactive contact deletion
    Інтерактивне видалення контакту
    """
    print(f"\n{Fore.RED}❌ {DELETING_CONTACT}")

    name = input(f"{Fore.CYAN}{ENTER_NAME}").strip()
    if not name:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
        return

    contact = assistant.contacts.find_contact(name)
    if not contact:
        print(f"{Fore.RED}❌ {CONTACT_NOT_FOUND}")
        return

    print(f"\n{Fore.YELLOW}ℹ️ Found contact:\n{contact}")
    confirm = input(f"{Fore.RED}{CONFIRM_DELETE}").lower().strip()

    if confirm == "y":
        if assistant.contacts.delete_contact(name):
            print(f"{Fore.GREEN}✅ {CONTACT_DELETED}")
        else:
            print(f"{Fore.RED}❌ Failed to delete contact")
    else:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")


def show_search_results(matches):
    """
    Shows search results in a formatted way
    Показує результати пошуку у форматованому вигляді
    Args:
        matches (list): List of found contacts / Список знайдених контактів
    """
    if matches:
        print(f"\n{Fore.GREEN}✅ Found {len(matches)} contact(s):")
        for i, contact in enumerate(matches, 1):
            print(f"{Fore.MAGENTA}{i}. {contact}")
    else:
        print(f"{Fore.RED}❌ {CONTACT_NOT_FOUND}")


def search_contacts_interactive(assistant):
    """
    Interactive contact search
    Інтерактивний пошук контактів
    """
    print(f"\n{Fore.YELLOW}🔍 {SEARCHING_CONTACTS}")
    print(f"{Fore.CYAN}Available search criteria:")
    print(f"{Fore.CYAN}1. By name")
    print(f"{Fore.CYAN}2. By phone")
    print(f"{Fore.CYAN}3. By email")

    choice = input(ENTER_SEARCH_CRITERIA).strip()
    if not choice:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
        return

    if choice == "1":
        name = input(f"{Fore.CYAN}Enter full or partial name: ").strip()
        if not name:
            print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
            return
        matches = assistant.contacts.find_contacts(name)

    elif choice == "2":
        phone = input(f"{Fore.CYAN}Enter full or partial phone number: ").strip()
        if not phone:
            print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
            return
        matches = assistant.contacts.find_by_phone(phone)

    elif choice == "3":
        email = input(f"{Fore.CYAN}Enter full or partial email: ").strip()
        if not email:
            print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
            return
        matches = assistant.contacts.find_by_email(email)

    else:
        print(f"{Fore.RED}❌ {INVALID_CHOICE}")
        return

    show_search_results(matches)


def show_birthdays_interactive(assistant):
    """
    Interactive birthday reminder
    Інтерактивний показ днів народження
    """
    print(f"\n{Fore.CYAN}🎂 Birthday reminder")

    days = input(f"{Fore.CYAN}Enter number of days to check (press Enter to cancel): ").strip()
    if not days:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
        return

    if not days.isdigit():
        print(f"{Fore.RED}❌ Please enter a valid number")
        return
    contacts = assistant.contacts.find_birthday_in_days(int(days))
    show_search_results(contacts)
   
