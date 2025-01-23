class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\nAdd New Contact")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self):
        search_term = input("\nEnter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found for '{search_term}'.")

    def update_contact(self):
        name = input("\nEnter the name of the contact to update: ")
        contact = next((contact for contact in self.contacts if contact.name.lower() == name.lower()), None)

        if contact:
            print(f"\nUpdating contact for {contact.name}")
            contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            print(f"Contact for {contact.name} updated successfully!")
        else:
            print(f"Contact for {name} not found.")

    def delete_contact(self):
        name = input("\nEnter the name of the contact to delete: ")
        contact = next((contact for contact in self.contacts if contact.name.lower() == name.lower()), None)

        if contact:
            self.contacts.remove(contact)
            print(f"Contact for {contact.name} deleted successfully!")
        else:
            print(f"Contact for {name} not found.")

    def menu(self):
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting the Contact Book. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

def main():
    contact_book = ContactBook()
    contact_book.menu()

if __name__ == "__main__":
    main()
