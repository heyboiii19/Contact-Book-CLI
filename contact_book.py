# Command-Line Contact Book Application
# Internship Task - Python File Handling

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {phone} | {email}\n")

    print("\n✅ Contact added successfully!\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("\n📭 No contacts found.\n")
                return

            print("\n📒 Contact List:")
            print("-" * 40)
            for contact in contacts:
                print(contact.strip())
            print("-" * 40)

    except FileNotFoundError:
        print("\n⚠ No contact file found.\n")


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                if search_name in contact.lower():
                    print("\n🔍 Contact Found:")
                    print(contact.strip())
                    found = True

        if not found:
            print("\n❌ Contact not found.\n")

    except FileNotFoundError:
        print("\n⚠ No contact file found.\n")


def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("\n👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
