#TASK - 5 
#CONTACT BOOK

contacts={}
def add_contact():
  name=input("Enter Name: ").title()
  phone_number=input("Enter Phone Number: ")
  email=input("Enter E-mail: ")
  address=input("Enter Address: ")

  contact={
    'Name':name,
    'Phone Number' : phone_number,
    'Email' : email,
    'Address' : address}
  contacts[name]=contact
  print(f"Contact of {name} added successfully!\n")

def view_contact_list():
  print("\nContacts List:\n")
  if contacts=={}:
    print("Your contact list is empty.")
  else:
    for name, contact in contacts.items():
      print(f"{name} - {contact['Phone Number']}")
  print()

def search_contact():
  query=input("Enter the Name or Phone Number to search: ").title()
  search_result=[]
  for name, contact in contacts.items():
    if query in name or query in contact['Phone Number']:
      search_result.append((name, contact))
  if search_result!=[]:
    print("Search Results:\n")
    for result in search_result:
      print(f"{result[0]} - {result[1]['Phone Number']}")
  else:
      print("No Matching Contact Found.\n")

def update_contact():
  query=input("Enter the Name or Phone Number of the contact to update: ").title()
  for contact in contacts.values():
    if query in contact['Phone Number']:
      query=contact['Name']
  
  if query in contacts.keys():
    print("\nConatct details:\n")
    print_contact_details(contacts[query])
    print("\nUpdate Details:")
    contacts[query]['Name']=input("Name: ")
    contacts[query]['Phone Number']=input("Phone Number: ")
    contacts[query]['Email']=input("Email: ")
    contacts[query]['Address']=input("Address: ")
    print("\nContact Details Updated Successfully!")
  else:
    print("Contact not found!")

def delete_contact():
  query=input("Enter the Name or Phone number of the contact to delete: ").title()
  for contact in contacts.values():
    if query in contact['Phone Number']:
      query=contact['Name']
      
  if query in contacts:
    print("Contact Details: ")
    print_contact_details(contacts[query])

    confirm=input("\nAre you sure you want to delete the contact? (y/n): ").lower()
    if confirm=='y':
      del contacts[query]
      print("Contact deleted Successfully!")
    else:
      print("Deletion Cancelled.")
  else:
    print("\nContact not Found.\n")

def print_contact_details(contact):
  print(f"Name = {contact['Name']}")
  print(f"Phone Number = {contact['Phone Number']}")
  print(f"E-Mail = {contact['Email']}")
  print(f"Address = {contact['Address']}")


def main():  
  while True:
    print("\n1.Add Contacts")
    print("2.View Contact List.")
    print("3.Search contact List")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    try:
      choice=int(input("Enter your choice(1-6): "))
    except:
      print("Invalid input. Make sure your choice is an integer and in range(1-6).")
      continue

    if choice == 1:
      add_contact()
    elif choice == 2:
      view_contact_list()
    elif choice == 3:
      search_contact()
    elif choice == 4:
      update_contact()
    elif choice == 5:
      delete_contact()
    elif choice == 6:
      break
    else:
      print("\nInvalid Choice. Choose between(1-6)!")

if __name__=='__main__':
  main()
