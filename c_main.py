from modules.assistant.assistant import PersonalAssistant
from modules.utils.messages import *
from modules.utils.interactive import (
    add_contact_interactive,
    edit_contact_interactive,
    delete_contact_interactive,
    search_contacts_interactive,
    show_birthdays_interactive,
)


def main():
    """
    Main function of the assistant
    Головна функція асистента
    """
    assistant = PersonalAssistant()
    print(WELCOME_MESSAGE)

    while True:
        mode = input(ENTER_MODE).lower().strip()

        if mode == "exit":
            print(GOODBYE_MESSAGE)
            break

        elif mode == "contacts":
            print("\nEntering contacts mode (type 'help' for available commands)")
            while True:
                try:
                    command = input(ENTER_COMMAND).lower().strip()

                    if command == "back":
                        break
                    elif command == "help":
                        print(HELP_MESSAGE)
                    elif command == "add":
                        add_contact_interactive(assistant)
                    elif command == "edit":
                        edit_contact_interactive(assistant)
                    elif command == "delete":
                        delete_contact_interactive(assistant)
                    elif command == "search":
                        search_contacts_interactive(assistant)
                    elif command == "all":
                        contacts = assistant.contacts.get_all_contacts()
                        if contacts:
                            print("\nAll contacts:")
                            for contact in contacts:
                                print(f"\n{contact}")
                        else:
                            print(NO_CONTACTS)
                    elif command == "birthdays":
                        show_birthdays_interactive(assistant)
                    else:
                        print(INVALID_COMMAND_MESSAGE)

                except Exception as e:
                    print(f"An error occurred: {e}")

        elif mode == "notes":
            print(NOT_IMPLEMENTED_MESSAGE.format("Notes mode"))

        else:
            print(INVALID_MODE_MESSAGE)


if __name__ == "__main__":
    main()
