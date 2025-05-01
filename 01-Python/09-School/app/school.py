from course import Course
from teacher import Teacher

class School:
    def __init__(self, name, students=None, teachers=None, courses=None):
        self.name = name
        self.students = students if students is not None else []
        self.teachers = teachers if teachers is not None else []
        self.courses = courses if  courses is not None else []

    def add_to_school(self, collection, item, role):
        collection.append(item)
        print(f"{item.name} est maintenant {role} à l'école {self.name}")

    def add_student(self, student):
        self.add_to_school(self.students, student, "étudiant")

    def add_teacher(self, teacher_name):
        teacher = Teacher.from_input(teacher_name)
        self.add_to_school(self.teachers, teacher, "professeur") 

    def add_course(self, course_name):
        course = Course.from_input(course_name)
        self.add_to_school(self.courses, course, "enseigné")

    def display_courses(self):
        for course in self.courses:
            print(f" id = {course.course_id} - {course.name}")

    def display_teachers(self):
        for teacher in self.teachers:
            print(f"{teacher.name}")

    @classmethod
    def from_input(cls, school_name):
        return cls(school_name)
