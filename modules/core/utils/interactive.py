from datetime import datetime, date, timedelta
from modules.core.constants.commands import DATE_FORMAT
from modules.core.fields import Phone, Email, Address, Birthday
from modules.core.constants.messages import *
from modules.core.utils.input_manager import input_with_validation
from colorama import Fore, Style, init

from modules.core.utils.table_viewer import TableViewer


def add_contact_interactive(assistant):
    """
    Interactive contact addition with field validation loops
    Інтерактивне додавання контакту з циклами перевірки полів
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

    # Phone input with validation loop / Введення телефону з циклом перевірки
    phones = None
    while True:
        phones_input = input(
            f"{Fore.CYAN}Enter phone numbers (10 digits, comma-separated) or press Enter to skip: "
        ).strip()
        if not phones_input:
            break

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

        phones = valid_phones
        break

    # Email input with validation loop / Введення пошти з циклом перевірки
    email = None
    while True:
        email_input = input(f"{Fore.CYAN}{ENTER_EMAIL}").strip()
        if not email_input:
            break

        if Email.validate(email_input):
            email = email_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_EMAIL}")

    # Address input with validation loop / Введення адреси з циклом перевірки
    address = None
    while True:
        address_input = input(f"{Fore.CYAN}{ENTER_ADDRESS}").strip()
        if not address_input:
            break

        if Address.validate(address_input):
            address = address_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_ADDRESS}")

    # Birthday input with validation loop / Введення дня народження з циклом перевірки
    birthday = None
    while True:
        birthday_input = input(f"{Fore.CYAN}{ENTER_BIRTHDAY}").strip()
        if not birthday_input:
            break

        if Birthday.validate(birthday_input):
            birthday = birthday_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_DATE}")

    result = assistant.contacts.add_contact(name, address, phones, email, birthday)
    if result:
        print(f"{Fore.GREEN}✅ {CONTACT_ADDED}")


def edit_contact_interactive(assistant):
    """
    Interactive contact editing with field validation loops
    Інтерактивне редагування контакту з циклами перевірки полів
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

    # Phone input with validation loop / Введення телефону з циклом перевірки
    phones = None
    while True:
        phones_input = input(
            f"{Fore.CYAN}Enter phone numbers (10 digits, comma-separated) or press Enter to skip: "
        ).strip()
        if not phones_input:
            break

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

        phones = valid_phones
        break

    # Email input with validation loop
    email = None
    while True:
        email_input = input(f"{Fore.CYAN}{ENTER_EMAIL}").strip()
        if not email_input:
            break

        if Email.validate(email_input):
            email = email_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_EMAIL}")

    # Address input with validation loop
    address = None
    while True:
        address_input = input(f"{Fore.CYAN}{ENTER_ADDRESS}").strip()
        if not address_input:
            break

        if Address.validate(address_input):
            address = address_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_ADDRESS}")

    # Birthday input with validation loop
    birthday = None
    while True:
        birthday_input = input(f"{Fore.CYAN}{ENTER_BIRTHDAY}").strip()
        if not birthday_input:
            break

        if Birthday.validate(birthday_input):
            birthday = birthday_input
            break
        else:
            print(f"{Fore.RED}⚠️ {INVALID_DATE}")

    if assistant.contacts.update_contact(name, address, phones, email, birthday):
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
    Shows search results in a formatted table with fixed column order
    Показує результати пошуку у форматованій таблиці з фіксованим порядком стовпців
    """
    if not matches:
        print(f"{Fore.RED}❌ {CONTACT_NOT_FOUND}")
        return

    # Define fixed column order / Визначаємо фіксований порядок стовпців
    columns = ["Name", "Phones", "Email", "Address", "Birthday"]
    table_viewer = TableViewer(columns)
    table_data = []

    for contact in matches:
        contact_data = {
            "Name": str(contact.name),
            "Phones": (
                ", ".join(str(p) for p in contact.phones) if contact.phones else ""
            ),
            "Birthday": (
                contact.birthday.value.strftime(DATE_FORMAT) if contact.birthday else ""
            ),
            "Email": str(contact.email) if contact.email else "",
            "Address": str(contact.address) if contact.address else "",
        }
        table_data.append(contact_data)

    table_viewer.display_table(table_data, title=f"✅ Found {len(matches)} contact(s):")


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
    Interactive birthday reminder with tabular display
    Інтерактивний показ днів народження з табличним відображенням
    """
    print(f"\n{Fore.CYAN}🎂 Birthday reminder")

    days = input(
        f"{Fore.CYAN}Enter number of days to check (press Enter to cancel): "
    ).strip()
    if not days:
        print(f"{Fore.YELLOW}⚠️ {CANCELED_MESSAGE}")
        return

    if not days.isdigit():
        print(f"{Fore.RED}❌ Please enter a valid number")
        return

    contacts = assistant.contacts.find_birthday_in_days(int(days))
    if not contacts:
        print(f"{Fore.RED}❌ No birthdays in the next {days} days")
        return

    # Define fixed column order for birthday table / Визначаємо фіксований порядок стовпців для таблиці днів народження
    birthday_columns = ["Days until", "Name", "Birthday", "Phones", "Email", "Address"]
    table_viewer = TableViewer(birthday_columns)
    table_data = []

    today = date.today()

    for contact in contacts:
        # Calculate days until birthday / Розрахунок днів до дня народження
        birthday = contact.birthday.value
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days

        contact_data = {
            "Days until": f"{days_until} days",
            "Name": str(contact.name),
            "Birthday": birthday.strftime(DATE_FORMAT),
            "Phones": (
                ", ".join(str(p) for p in contact.phones) if contact.phones else ""
            ),
            "Email": str(contact.email) if contact.email else "",
            "Address": str(contact.address) if contact.address else "",
        }
        table_data.append(contact_data)

    table_viewer.display_table(
        table_data, title=f"🎂 Birthdays in the next {days} days:"
    )
