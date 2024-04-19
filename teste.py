'''import re

def email_valid(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-z.]+$'
    return bool(re.match(pattern, email))

# Função para preencher o email
def preencher_email():
    while True:
        email = input("Digite seu endereço de email: ")
        if email_valid(email):
            print("Email válido!")
            return email
        else:
            print("Por favor, digite um email válido.")

# Exemplo de uso da função preencher_email
email_usuario = preencher_email()
print("O email inserido foi:", email_usuario)'''

def add_task(tasks, statistics):

  task = {"task": statistics, "completed": False}
  tasks.append(task)
  print (f"{statistics} sucessfull added!")
  return 

def view_tasks(tasks):
  print("\n List of taks:")
  for index, task in enumerate(tasks, start=1):
    status = "✔" if task["completed"] else " "
    name_task = task["task"]
    print(f"{index} [{status}] {name_task}")

tasks = []
while True:
  print ("\n Menu do Gerenciador de Lista de tarefas:")
  print ("1. Adicionar Tarefa")
  print ("2. Ver tarefas")
  print ("3. Atualizar Tarefa")
  print ("4. Completar Tarefa")
  print ("5. Remover Tarefa completas")
  print ("6. Sair")

  choise = input("Digite a sua escolha: ")

  if choise == "1":
    statistics = input("Enter the name of the task you want to add: ")
    add_task(tasks, statistics)

  elif choise == "2":
    view_tasks(tasks)