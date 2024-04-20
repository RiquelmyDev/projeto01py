import re
def email_valid(em):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-z.]+$"
    return bool(re.match(pattern, em))


def number_valid(num):
  regex = r"^[0-9]+$"
  return bool(re.match(regex, num))


contacts = []

def add_contact(nick, num, em):

  contact = {"name": nick, "number": num, "email": em, "favorite": False}
  contacts.append(contact)
  print(f"{nick} sucessfull added.")
  return

def view_contacts():
  print("\n Contact List: ")
  for index, contact in enumerate(contacts,start=1):
    status = "★" if contact["favorite"] else " "
    print(f"{index} {contact["name"]} {contact["number"]} {contact["email"]}  [{status}]")

def edit_contact(contacts, index_contact, new_name, new_number, new_email):
  contact_review = int(index_contact) - 1
  if contact_review >= 0 and contact_review < len(contacts):
    contacts[contact_review]["name"] = new_name
    contacts[contact_review]["number"] = new_number
    contacts[contact_review]["email"] = new_email
    print(f"\n Contact {index_contact} uptade Success!")
  else:
    print("INVALID CONTACT INDEX")

def favorite_contact(contacts, index_contact):
  contact_review = int(index_contact) - 1
  contacts[contact_review]["favorite"] = True
  print(f"Contact {contacts[contact_review]['name']} marked as Favorite!")
  return

def view_favorite(contacts):
  favorite_contacts = [contact for contact in contacts if contact["favorite"] == True]
  if favorite_contacts:
    print("\n Favorite Contacts: ")
    for index, contacts in enumerate(favorite_contacts, start=1):
      print (f"{index} {contacts["name"]} {contacts["number"]} {contacts["email"]}")

def delete_contact(contacts):
    contacts_to_delete = []
    for contact in contacts:
        confirm = input(f"Do you want to delete {contact['name']}? (yes/no): ")
        if confirm.lower() == "yes":
            contacts_to_delete.append(contact)

    for contact in contacts_to_delete:
        contacts.remove(contact)
    print("Completed contacts were deleted!")
    return

while True:
  print("\n Contact Agenda")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Edit Contacts")
  print("4. Favorite Contacts")
  print("5. View Contacts Favorits")
  print("6. Delete Contacts")

  choise = input("Enter your choice: ")

  if choise == "1":
    nick = input("Add contact name: ")
    num = input("Phone number: ")
    em = input("Email address: ")
    if email_valid(em) and number_valid(num):
      add_contact(nick, num, em) 
    else:
      print("Invalid email address or phone number. Please enter valid information...")
  
  elif choise == "2":
    view_contacts()


  elif choise ==  "3":
    view_contacts()
    index_contact = input("Enter the index of contact you want to update: ")
    new_name = input("Enter the new name of this contact: ")
    new_number = input("Enter the new number of this contact: ")
    new_email = input("Enter the new email of this contact: ")
    edit_contact(contacts, index_contact, new_name, new_number, new_email)
    """if new_email_valid(new_email) and new_number_valid(new_number):
    else:
      print("Invalid email address or phone number. Please enter valid information...")"""

  elif choise == "4":
    view_contacts()
    index_contact = input("Enter the contact you want to Favorite: ")
    favorite_contact(contacts, index_contact)

  elif choise == "5":
    view_favorite(contacts)

  elif choise == "6":
    delete_contact(contacts)
    view_contacts()


  elif choise == "7":
      print("Exiting...")
      break
      

print ("Agenda Finished")
