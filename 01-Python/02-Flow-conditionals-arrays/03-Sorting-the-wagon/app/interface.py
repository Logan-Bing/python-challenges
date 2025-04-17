from sorting_wagon import wagon_sort

def interface():

    students = []

    while True:
        name = input()
        if name == "":
            break
        students.append(name)
        print('Type another student name or press enter to finish:')

    sorted_students = wagon_sort(students)
    print(f"\nCongratulations! Your Wagon has {len(sorted_students)} student{'s' if len(sorted_students) > 1 else ''}:")

    if len(sorted_students) == 1:
        print(sorted_students[0])
    elif len(sorted_students) == 2:
        print(f"{sorted_students[0]} and {sorted_students[1]}")
    else:
        print(f"{', '.join(sorted_students[:-1])} and {sorted_students[-1]}")

interface()
