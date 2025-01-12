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
from modules.core.utils.table_viewer import TableViewer


def main():
    """
    Main function of the assistant
    Головна функція асистента
    """
    init(autoreset=True)  # Initialize colorama
    assistant = PersonalAssistant()
    print(f"{Fore.GREEN}{Style.BRIGHT}👋 {WELCOME_MESSAGE}")

    while True:
        mode = input(f"{Fore.CYAN}{ENTER_MODE}").lower().strip()

        if mode == EXIT_COMMAND:
            print(f"{Fore.RED}👋 {GOODBYE_MESSAGE}")
            break

        elif mode == CONTACTS_MODE:
            print(
                f"\n{Fore.YELLOW}📇 Entering contacts mode (type 'help' for available commands)"
            )
            while True:
                try:
                    command = input(f"{Fore.CYAN}{ENTER_COMMAND}").lower().strip()

                    if command == BACK:
                        print(f"{Fore.YELLOW}🔙 Returning to main menu.")
                        break
                    elif command == HELP:
                        print(f"{Fore.GREEN}ℹ️ {HELP_MESSAGE}")
                        # assistant.display_commands()
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
                            birthday_columns = [
                                "Name",
                                "Phones",
                                "Email",
                                "Address",
                                "Birthday",
                            ]
                            table_viewer = TableViewer(birthday_columns)
                            table_data = []
                            for contact in contacts:
                                contact_data = {
                                    "Name": str(contact.name),
                                    "Phones": (
                                        ", ".join(str(p) for p in contact.phones)
                                        if contact.phones
                                        else ""
                                    ),
                                    "Birthday": (
                                        contact.birthday.value.strftime(DATE_FORMAT)
                                        if contact.birthday
                                        else ""
                                    ),
                                    "Email": (
                                        str(contact.email) if contact.email else ""
                                    ),
                                    "Address": (
                                        str(contact.address) if contact.address else ""
                                    ),
                                }
                                table_data.append(contact_data)
                            table_viewer.display_table(
                                table_data, title=f"{Fore.MAGENTA}📋 All contacts:"
                            )
                        else:
                            print(NO_CONTACTS)
                    elif command == BIRTHDAYS:
                        show_birthdays_interactive(assistant)
                    else:
                        print(f"{Fore.RED}⚠️ {INVALID_COMMAND_MESSAGE}")

                except Exception as e:
                    print(f"{Fore.RED}⚠️ An error occurred: {e}")

        elif mode == NOTES_MODE:
            print(
                f"\n{Fore.YELLOW}📝 Entering notes mode (type 'help' for available commands)"
            )
            while True:
                try:
                    command = input(f"{Fore.CYAN}{ENTER_COMMAND}").lower().strip()

                    if command == BACK:
                        print(f"{Fore.YELLOW}🔙 Returning to main menu.")
                        break
                    elif command == HELP:
                        print(f"{Fore.GREEN}ℹ️ Available commands:")
                        for command, description in assistant.commands.items():
                            print(f"{Fore.CYAN}{command}: {description}")
                    elif command == ADD_NOTE:
                        text = input("Enter note text: ")
                        tags = input("Enter tags (comma separated): ").split(",")
                        assistant.notes.add_note(text, tags)
                    elif command == ALL_NOTES:
                        notes = assistant.notes.notes
                        if notes:
                            columns = ["ID", "Text", "Tags"]
                            table_viewer = TableViewer(columns)
                            table_data = []
                            for note in notes:
                                table_data.append({
                                    "ID": note.id,
                                    "Text": note.text,
                                    "Tags": note.tags,
                                })
                            table_viewer.display_table(
                                table_data, title=f"{Fore.MAGENTA}📋 All notes:"
                            )
                        else:
                            print(f"{Fore.YELLOW}No notes available.")
                    elif command == EDIT_NOTE:
                        note_id = input("Enter note id: ")
                        new_text = input("Enter new text: ")
                        assistant.notes.edit_note(note_id, new_text)
                        print(f"Note edited successfully. {note_id}")
                    elif command == DELETE_NOTE:
                        note_id = input("Enter note id: ")
                        assistant.notes.delete_note(note_id)
                        print(f"Note deleted successfully. {note_id}")
                    elif command == SEARCH_NOTE_BY_TEXT:
                        search_text = input("Enter text to search in notes: ")
                        results = assistant.notes.search_note_by_text(search_text)
                        if results:
                            print("Found notes:")
                            for note in results:
                                print(note)
                        else:
                            print("No notes found containing the given text.")
                    elif command == EDIT_NOTE_TAGS:
                        note_id = input("Enter note ID: ")
                        new_tags = input("Enter new tags (comma separated): ").split(",")
                        assistant.notes.edit_note_tags(note_id, new_tags)
                        print("Tags updated successfully!")
                    elif command == SEARCH_BY_TAG:
                        tag = input("Enter tag to search: ")
                        results = assistant.notes.search_by_tag(tag)
                        if results:
                            print("\nNotes with tag:", tag)
                            for note in results:
                                print(note)
                        else:
                            print("No notes found with this tag.")
                    elif command == FILTER_BY_TAG:
                        tag = input("Enter tag to filter notes: ")
                        results = assistant.notes.filter_notes_by_tag(tag)
                        if results:
                            print("Notes with tag '{}' found:".format(tag))
                            for note in results:
                                print(note)
                        else:
                            print("No notes found with the tag '{}'.".format(tag))
                    elif command == SORT_BY_TAGS:
                        sorted_notes = assistant.notes.sort_by_tags()
                        print("\nNotes sorted by number of tags:")
                        for note in sorted_notes:
                            print(note)
                    else:
                        print(
                            f"{Fore.RED}⚠️ Invalid action. Please choose a valid command."
                        )
                except Exception as e:
                    print(f"{Fore.RED}⚠️ An error occurred: {e}")

        else:
            print(f"{Fore.RED}⚠️ {INVALID_MODE_MESSAGE}")



if __name__ == "__main__":
    main()
