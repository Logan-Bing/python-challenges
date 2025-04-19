
contacts = {}
user_choice = ""
user_choice_contact = ""

def display_contact(contacts: dict) -> None:
    print("---MES CONTACTS---")
    for name, num in contacts.items():
        print(f"{name} - {num}")

def add_contact(name: str, num: str) -> None:
    contacts[name] = num

def search_with_name(name: str, contacts: dict ) -> str:
    return f"{name} - {contacts[name]}"

def delete_contact(name: str, contacts: dict) -> None:
    del contacts[name]

while True:

    print("---MON REPERTOIRE---")
    print("1 - Ajouter un contact")
    print("2 - Rechercher un contact")
    print("3 - Supprimer un contact")
    print("4 - Afficher tous les contacts")
    print("5 - Quitter")
    user_choice = input("Selectionner un choix: ")

    if user_choice == '1':
        print("Entrer le nom de votre contact:")
        contact_name = input(">> ")
        print(f"Entrer le numéro de {contact_name}:")
        contact_num = input(">> ")
        add_contact(contact_name, contact_num)
        print("Votre contact est bien enregisté")
    elif user_choice == '2':
        print("Choisissez votre méthode de recherche")
        print("1-Recherche avec le nom")
        print("2-Recherche avec le numéro")
        user_choice_contact = input(">> ")
        if user_choice_contact == "1":
            print("Entrer le nom de votre contact")
            search_name = input(">> ")
            print(search_with_name(search_name, contacts))
        elif user_choice_contact == "2":
            print("Entrer le numéro de votre contact")
            search_num = input(">> ")
            for name, num in contacts.items():
                if num == search_num:
                    print(f"{name} - {num}")
    elif user_choice == '3':
        print(display_contact(contacts))
        print("------------------")
        print("Entrer le nom du contact que vous voulez supprimer")
        contact_del = input(">> ")
        delete_contact(contact_del, contacts)
        print(f"{contact_del} a bien été supprimé")
    elif user_choice == '4':
        print(display_contact(contacts))
        print("------------------")
    elif user_choice == '5':
        print("------------------")
        print("A BIENTOT")
        print("------------------")
        break
