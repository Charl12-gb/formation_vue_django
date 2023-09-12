# Voici un exemple minimaliste de code pour illustrer ces étapes :

import pickle

# Charger les tâches depuis le fichier ou initialiser une liste vide
try:
    with open("tasks.pkl", "rb") as file:
        tasks = pickle.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

def create_task(description):
    tasks.append(description)
    save_tasks()

def read_tasks():
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def update_task(index, new_description):
    tasks[index] = new_description
    save_tasks()

def delete_task(index):
    del tasks[index]
    save_tasks()

while True:
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Choose an option : ")

    if choice == "1":
        print("----------------------ADD TASK---------------------------------")
        task_description = input("Enter task description : ")
        create_task(task_description)
        print("-----------------------------------------------------------------\n")
    elif choice == "2":
        print("----------------------TASK LIST----------------------------------")
        read_tasks()
        print("-----------------------------------------------------------------\n")
    elif choice == "3":
        print("---------------------UPDATE TASK---------------------------------")
        read_tasks()
        task_index = int(input("Enter the number of the task to be updated : ")) - 1
        new_description = input("Enter new description : ")
        update_task(task_index, new_description)
        print("-----------------------------------------------------------------\n")
    elif choice == "4":
        print("---------------------DELETE TASK---------------------------------")
        read_tasks()
        task_index = int(input("Enter the number of the job to be deleted : ")) - 1
        delete_task(task_index)
        print("-----------------------------------------------------------------\n")
    elif choice == "5":
        print("-----------------------GOOD BYE--------------------------------\n")
        break
    else:
        print("Invalid option. Please choose again.")

# Ceci est un exemple très basique, mais vous pouvez construire sur cette base en ajoutant plus de fonctionnalités, 
# de validation des entrées utilisateur, et en rendant l'interface plus conviviale. 
# Vous pourriez également envisager d'utiliser une bibliothèque comme `click` pour améliorer la gestion des commandes et des arguments en ligne de commande.