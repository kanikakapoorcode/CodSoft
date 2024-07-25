#contact-Book using python
class Contact :
    def __init__(self, name, phone, email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
    def __str__(self) :
        return f"Name: {self.name} - {self.phone}"
    
    
    
class ContactBook :
    def __init__(self):
        self._contacts = []
        
    def add_contact(self , name , phone , email , address) :
        contact = Contact(name, phone, email, address)
        self._contacts.append(contact)
        print(f"Contact {name} added successfully ! ")
        
    def view_contact_list(self) :
        if not self._contacts :
            print("No contacts in the book ! ")
        else :
            print("Contact List : ")
            for i , contact in enumerate(self._contacts, start=1) :
                print(f"{i} - {contact}")
    
    def search_contact(self , query):
            results = [contact for contact in self.contacts if query in contact.name or query in contact.phone] 
            if not results :
                print("No contacts found .")
            else :
                print("Search results : ")
                for i , contact in enumerate(results, start=1) :
                    print(f"{i} - {contact}")
                    
    
    def update_contact(self, name):
      for contact in self.contacts:
        if contact.name == name:
            print("Enter new values (press Enter to skip):")
            new_name = input(f"Name ({contact.name}): ")
            new_phone_number = input(f"Phone Number ({contact.phone_number}): ")
            new_email = input(f"Email ({contact.email}): ")
            new_address = input(f"Address ({contact.address}): ")
            
            if new_name != "":
                contact.name = new_name
            if new_phone_number != "":
                contact.phone_number = new_phone_number
            if new_email != "":
                contact.email = new_email
            if new_address != "":
                contact.address = new_address
            print(f"Contact {name} updated successfully!")
            return
    print("Contact not found.")
        
        
    
    def delete_contact(self , name):
        for contact in self.contacts :
            if contact.name == name :
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully !")
                return
        print("Contact not Found.")
        
        
def main() :
        print("------------------------------------------\n")
        print("--------Welcome to the Address Book !-----")
        print("\n------------------------------------------")
        
        contact_book = ContactBook()
        
        print("Please select the option---->\n : Contact Book Menu")
        
        while True :
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Quit")
            
            
            choice = input("Choose an Option :")
            
            if choice == '1' :
                name = input("Enter the name : ")
                phone = input("Enter the phone number : ")
                email = input("Enter the email : ")
                address = input("Enter the address : ")
                contact_book.add_contact(name , phone , email , address)
            
            elif choice == '2' :
                contact_book.view_contacts()
            
            elif choice == '3' :
                query = input("Enter Search Query :")
                contact_book.search_contact(query)
            
            elif choice == '4' :
                name = input("Enter name of contact to update: ")
                contact_book.update_contact(name)
                
            
            elif choice == '5' :
                name = input("Enter name of contact to delete : ")
                contact_book.delete_contact(name)
                
            
            elif choice == '6' :
                print("GoodBye !!")
                break 
            
            else :
                print("Invalid Choice. Please Choose Again .")

if __name__ == "__main__" :
     main()  

                
        