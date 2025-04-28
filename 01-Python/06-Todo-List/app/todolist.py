
def save_tasks(todoList):
    with open("tasks.txt", "w") as f:  # "w" écrase pour repartir propre
        for task in todoList:
            line = f"{task['name']},{task['category']},{task['priority']},{task['completed']}\n"
            f.write(line)

def load_tasks():
    todoList = []
    with open("tasks.txt", "r") as f:
        for line in f:
            name, category, priority, completed = line.strip().split(",")
            todoList.append({
                "name": name,
                "category": category,
                "priority": int(priority),
                "completed": completed == "True"
            })
    return todoList


def addTask(name, category, priority, todoList) -> None :
    new_task = {'name': name, 'category': category, 'priority': priority, 'completed': False}
    todoList.append(new_task)

def markTaskAsDone(taskName, todoList) -> None :
    for todo in todoList:
        if todo["name"] == taskName:
            todo["completed"] = True
            break


def deleteTask(taskName, todoList) -> None:
    for i in range(len(todoList)):
        if todoList[i]["name"] == taskName:
            del todoList[i]
            break

def displayTasks(todoList) -> str:
    for todo in todoList:
        print(f" nom: {todo['name']} - categorie: {todo['category']} - priority: {todo['priority']} - Statut: {todo['completed']}")

def displayByPriority(todoList):
    priority_sorted = sorted(todoList, key=lambda todo: todo['priority'] )
    all_priority = set()
    for todo in priority_sorted:
        all_priority.add(todo['priority'])
    for priority in all_priority:
        print(priority)

def displayByCategory(todoList):
    categories = [todo['category'] for todo in todoList]
    for category in set(categories):
        print(category)

def displayIncompleteTasks(todoList):
    filtred_incomplete_tasks = [todo for todo in todoList if todo['completed'] == False]
    for todo in filtred_incomplete_tasks:
        print(f" nom: {todo['name']} - categorie: {todo['category']} - priority: {todo['priority']} - Statut: {todo['completed']}")

def selectCategory(category, todoList):
    filtred_category = [todo for todo in todoList if todo['category'] == category]
    for todo in filtred_category:
        print(f" nom: {todo['name']} - categorie: {todo['category']} - priority: {todo['priority']} - Statut: {todo['completed']}")

def selectPriority(priority, todoList):
    filtred_priority = [todo for todo in todoList if todo['priority'] == priority]
    for todo in filtred_priority:
        print(f" nom: {todo['name']} - categorie: {todo['category']} - priority: {todo['priority']} - Statut: {todo['completed']}")



todoList = []


while True:

    print("============ TODO LIST ============")
    print("1 - Ajouter une tâche ")
    print("2 - Afficher toutes mes tâches ")
    print("3 - Marquer une tâche comme faite ")
    print("4 - Supprimer une tâche ")
    print("5 - Quitter ")
    print("====================================")

    user_select = input("Selectionner une option: ")

    if user_select == "1":
        task_name = input("Entrer le nom de votre tâche: ")
        task_category = input("Entrer la category de votre tâche: ")
        task_priority = input("Définir la priorité de votre tâche (1 - 5): ")
        addTask(task_name, task_category, int(task_priority), todoList)
    elif user_select == "2":
        print("1 - Afficher toute les tâches")
        print("2 - Afficher toute les tâches par catégories")
        print("3 - Afficher toute les tâches par priorité")
        user_display_choice = input("Comment voulez vous qu'apparaisse vos tâches ? ")
        if user_display_choice == "1":
            displayTasks(todoList)
        elif user_display_choice == "2":
            displayByCategory(todoList)
            user_category_choice = input("Choisissez une catégorie: ")
            selectCategory(user_category_choice, todoList)
        else:
            displayByPriority(todoList)
            user_priority_choice = input("Choisissez une priorité: ")
            selectPriority(int(user_priority_choice), todoList)
    elif user_select == "3":
        displayIncompleteTasks(todoList)
        task_done_choice = input("Entrer le nom de la tâche qui est complété: ")
        markTaskAsDone(task_done_choice, todoList)
    elif user_select == "4":
        displayTasks(todoList)
        user_delete_choice = input("Entrer le nom de la tâche que vous voulez supprimer: ")
        deleteTask(user_delete_choice, todoList)
    elif user_select == "5":
        print('A bientot !')
        break

    save_tasks(todoList)
