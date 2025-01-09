from colorama import Fore, Style, init
from modules.assistant.assistant import PersonalAssistant
from modules.core.constants.messages import *
from modules.core.constants.commands import *
from modules.core.utils.interactive import (
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
    print(f"{Fore.GREEN}{Style.BRIGHT}👋 {WELCOME_MESSAGE}")

    while True:
        mode = input(f"{Fore.CYAN}{ENTER_MODE}").lower().strip()

        if mode == EXIT_COMMAND:
            print(f"{Fore.RED}👋 {GOODBYE_MESSAGE}")
            break

        elif mode == CONTACTS_MODE:
            print(f"\n{Fore.YELLOW}📇 Entering contacts mode (type 'help' for available commands)")
            while True:
                try:
                    command = input(f"{Fore.CYAN}{ENTER_COMMAND}").lower().strip()

                    if command == BACK:
                        print(f"{Fore.YELLOW}🔙 Returning to main menu.")
                        break
                    elif command == HELP:
                        print(f"{Fore.GREEN}ℹ️ {HELP_MESSAGE}")
                    elif command == ADD_CONTACT:
                        add_contact_interactive(assistant)
                    elif command == EDIT_CONTACT:
                        edit_contact_interactive(assistant)
                    elif command == DELETE_CONTACT:
                        delete_contact_interactive(assistant)
                    elif command == SEARCH_CONTACT:
                        search_contacts_interactive(assistant)
                    elif command == ALL_CONTACTS:
                        contacts = assistant.contacts.get_all_contacts()
                        if contacts:
                            print(f"\n{Fore.MAGENTA}📋 All contacts:")
                            for contact in contacts:
                                 print(f"{Fore.WHITE}{contact}")
                        else:
                            print(NO_CONTACTS)
                    elif command == BIRTHDAYS:
                        show_birthdays_interactive(assistant)
                    else:
                        print(f"{Fore.RED}⚠️ {INVALID_COMMAND_MESSAGE}")

                except Exception as e:
                    print(f"{Fore.RED}⚠️ An error occurred: {e}")

        elif mode == NOTES_MODE:
            print(f"{Fore.YELLOW}📝 {NOT_IMPLEMENTED_MESSAGE.format('Notes mode')}")

        else:
            print(f"{Fore.RED}⚠️ {INVALID_MODE_MESSAGE}")


if __name__ == "__main__":
    main()
