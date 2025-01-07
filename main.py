from modules.assistant.assistant import PersonalAssistant

def main():
    assistant = PersonalAssistant()

    while True:
        print("\nPersonal Assistant")
        print("1. Add Contact")
        print("2. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (YYYY-MM-DD): ")
            assistant.add_contact(name, address, phone, email, birthday)
        
        elif choice == "2":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
