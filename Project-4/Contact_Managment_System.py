class Contact:
    def __init__(self,name,number,email):
        self.__name=name
        self.__number=number
        self.__email=email
    @property
    def name(self):
        return self.__name
    @property
    def number(self):
        return self.__number
    @property
    def email(self):
        return self.__email
    @name.setter
    def name(self,name):
        self.__name=name
    @number.setter
    def number(self,number):
        self.__number=number
    @email.setter
    def email(self,email):
        self.__email=email
        
    def display_contact(self):
            print(f"Name: {self.__name.title()}")
            print(f"Number: {self.__number}")
            print(f"Email: {self.__email}")

class ContactManager:
    def __init__(self):
        self.__contacts=[]

    def add_contact(self):
        name=input("Enter the Name: ").strip()
        number=input("Enter the Phone Number: ").strip()
        email=input("Enter Email: ").strip()

        contact=Contact(name,number,email)
        self.__contacts.append(contact)

        print("Contact Added successfully")
    def search_contact(self):
        search_name=input("Enter the you wnat to seaech: ").strip()

        for contact in self.__contacts:
            if contact.name.lower()==search_name.lower():
                print("\nContact Found")
                contact.display_contact()
                return 

        print("Contact Not found")
    def update_contact(self):
        name=input("Enter the Name You want to update").strip()

        for contact in self.__contacts:
            if contact.name.lower()==name.lower():
                print("\nCurrent Contact Details")
                contact.display_contact()

                new_name=input("Enter new name: ").strip()
                new_number=input("Enter new Number: ").strip()
                new_email=input("Enter new Email: ").strip()

                contact.name=new_name
                contact.number=new_number
                contact.email=new_email

                print("Contact Updated Success fully")
                return
        print("Contact Not found")
    def delete_contact(self):
        name=input("Enter the name you want to delete: ").strip()

        for contact in self.__contacts:
            if contact.name.lower==name:
                self.__contacts.remove(contact)
                print("Contact Deleted Successfully")
                return
        print("Contact not found")
    def view_contacts(self):
        if len(self.__contacts)==0:
            print("No Contacts found")
            return
        print("\n++++ALL CONTACTS++++")
        for contact in self.__contacts:
            print()
            contact.display_contact()
        print("________________________")

manager = ContactManager()

while True:
    print("\n+++++++ CONTACT MANAGEMENT SYSTEM +++++++")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.search_contact()

    elif choice == "3":
        manager.update_contact()

    elif choice == "4":
        manager.delete_contact()

    elif choice == "5":
        manager.view_contacts()

    elif choice == "6":
        print("Thank you for using Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")