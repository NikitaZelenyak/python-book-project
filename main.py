from modules.assistant.assistant import PersonalAssistant

def main():
    print("Welcome to your personal assistant!")

    assistant = PersonalAssistant()

    while True:
        mode = input("Select mode: ").lower().strip()

        if mode == "exit":
            break
        elif mode == "contacts":
            break
        elif mode == "notes":
            while True:
                command = input("Input your command: ").lower().strip()

                if command == "back":
                    break

                elif command == "all":
                    assistant.all_notes()

                elif command == "add":
                    assistant.add_note()

                elif command == "search":
                    break

                elif command == "sort":
                    break

                elif command == "edit":
                    assistant.edit_note()

                elif command == "delete":
                    assistant.delete_note()

                else:
                    print("Invalid action. Please choose add, search, sort, edit, or delete.")
        else:
            print("Invalid mode. Please choose contacts or notes.")


if __name__ == "__main__":
    main()
