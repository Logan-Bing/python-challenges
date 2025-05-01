
from student import Student
from teacher import Teacher
from course import Course
from school import School


while True:

    print("========== Bienvenue ============")
    print("1-Créer mon école")
    print("2-Quitter")
    print("=================================")
    user_choice = input("Choisissez une option : ")

    if user_choice == "1":
        school_name = input("Entrer le nom de votre école : ")
        school = School.from_input(school_name)
        print(f"L'école {school.name} ouvre ses portes ! ")

        while True:

            print(f"=============== Interface gestion de {school.name} =================== ")
            print(f"1-Ajouter un cours qui sera étudié a {school.name}")
            print(f"2-Ajouter un professeur qui enseignera a {school.name}")
            print(f"3-Ajouter un étudiant qui étudiera a {school.name}")
            print(f"4-Gérer les cours")
            print(f"5-Gérer les professeurs")
            print(f"6-Gérer les étudiants")
            print(f"7-Quitter")
            print("=================================")

            user_choice = input("Choisissez une option : ")

            if user_choice == "1":
                course_name = input("Entrer le nom d'une nouvelle matiére : ")
                course = school.add_course(course_name)
            elif user_choice == "2":
                teacher_name = input("Entrer le nom du nouveau profésseur")
                teacher = school.add_teacher(teacher_name)
            elif user_choice == "3":
                ...
            elif user_choice == "4":
                print(f"1-Afficher tout les cours étudié a {school.name}")
                print(f"2-Assigné un professeur à un cours")

                user_choice = input("Choisissez une option : ")

                if user_choice == "1":
                    print(f"============ Les cours enseigné à {school.name} ==================")
                    school.display_courses()
                    print("=================================")
                elif user_choice == "2":
                    print(f"============ Les cours enseigné à {school.name} ==================")
                    school.display_courses()
                    print("=================================")

                    course_choice = input("Entrer l'id du cours : ")

                    print(f"============ Les professeurs qui enseigne à {school.name} ==================")
                    school.display_teachers()
                    print("=================================")

                    teacher_choice = input("Entrer le nom du professeur : ")

                    for course in school.courses:
                        if course_choice == course.id:
                            course.report_teacher_assignement()

            elif user_choice == "5":
                print(f"1-Afficher tout les profésseur de {school.name}")

                user_choice = input("Choisissez une option : ")

                if user_choice == "1":
                    print(f"============ Les professeurs qui enseigne à {school.name} ==================")
                    school.display_teachers()
                    print("=================================")
            elif user_choice == "6":
                ...
            else:
                print("A bientôt")
                break

    else:
        print("A bientôt")
        break
