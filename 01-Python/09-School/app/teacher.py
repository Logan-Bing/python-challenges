from person import Person

class Teacher(Person):

    teacher_id = 1

    def __init__(self, name, age, courses=None):
        super().__init__(name, age)
        self.courses = courses if courses is not None else []
        Teacher.teacher_id += 1

    def add_note_to_student(self, student, note):
        if not (0 <= note <= 20):
            raise ValueError("La note doit être entre 0 et 20.")
        student.notes.append(note)
        print(f"{student.name} a eu la note de {note}")

    @classmethod
    def from_input(cls, teacher_name):
        return cls(teacher_name)
