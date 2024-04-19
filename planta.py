import re
def email_valid(em):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-z.]+$"
    return bool(re.match(pattern, em))

import re
def number_valid():
  regex = r"^[0-9]+$"
  input = "0123456789"


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

def favorite_contact(contacts, index_contact):
  contact_review = int(index_contact) - 1
  contacts[contact_review]["favorite"] = True
  print(f"Contact {"name"} marked as Favorite!")
  return
  

while True:
  print("\n Contact Agenda")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Favorite Contacts")
  print("4. Delete Contacts")

  choise = input("Enter your choice: ")

  if choise == "1":
    nick = input("Add contact name: ")
    num = input("Phone number: ")
    em = input("Email address: ")
    if email_valid(em):
      add_contact(nick, num, em)
    else:
      print("Invalid email address. Please enter a valid email.")
  
  elif choise == "2":
    view_contacts()

    
  elif choise == "3":
    view_contacts()
    index_contact = input("Enter the contact you want to Favorite: ")
    favorite_contact(contacts, index_contact)
      

print ("Agenda Finished")
