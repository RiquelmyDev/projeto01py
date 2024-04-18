def add_contact(nick, num, em):

  contact = {"name": nick, "number": num, "email": em, "favorite": False}
  contacts.append(contact)
  print(f"{nick} sucessfull added.")
  return

def view_contacts(contacts):
  print("\n Contact List: ")
  for index, contact in enumerate(contacts,start=1):
    favorite = "★" if contact["favorite"] else " "
 
    print (f"{index} {nick} {num} {em} [{favorite}]")

import re
def email_valid(em):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-z.]+$"
    return bool(re.match(pattern, em))

contacts = []
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
    view_contacts(contacts)
    
      

print ("Agenda Finished")
