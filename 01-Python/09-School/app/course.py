
class Course:

    course_id = 1

    def __init__(self, name, students=None, teacher=None):
        self.name = name
        self.students = students if students is not None else set()
        self.teacher = teacher
        Course.course_id += 1

    def set_teacher(self, teacher):
        if self.teacher is None:
            self.teacher = teacher
            return teacher
        return False

    def report_teacher_assignement(self, teacher):
        if self.set_teacher(teacher):
            return f"{teacher.name} enseigne maintenant le cours de {self.name}"
        else:
            return f"{self.teacher.name} enseigne déjà le cours de {self.name}"

    def assign_students(self, students):
        students_already_listed = [student for student in students if student in self.students]
        students_not_listed = [student for student in students if student not in self.students]

        self.students.update(students_not_listed)
        return students_already_listed, students_not_listed

    def report_students_assignments(self, students):
        already_listed, newly_added = self.assign_students(students)

        for student in already_listed:
            print(f"{student.name} est déjà inscrit au cours de {self.name}")

        for student in newly_added:
            print(f"{student.name} est maintenant inscrit au cours de {self.name}")

    def display_students_listed(self):
        for student in self.students:
            print(f"{student.name}")

    def calculate_course_average(self):
        total_notes = [student.calculater_notes_average() for student in self.students ]
        result = sum(total_notes) / len(total_notes)
        return result

    def display_course_average(self):
        return f"la moyenne du cour de {self.name} est de {self.calculate_course_average()}"

    @classmethod
    def from_input(cls, course_name):
        return cls(course_name)
