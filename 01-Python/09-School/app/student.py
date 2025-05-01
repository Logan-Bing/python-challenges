from person import Person

class Student(Person):
    def __init__(self, name, age, notes=None, courses=None):
        super().__init__(name, age)
        self.notes = notes if notes is not None else []
        self.courses = courses if courses is not None else []

    def calculater_notes_average(self):
        result = sum(self.notes) / len(self.notes)
        return result

    def display_average(self):
        return f"La moyenne de {self.name} est de {self.calculater_notes_average()}"
    