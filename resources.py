from typing import List

RESOURCE_TYPES = ("Laptop", "Book", "Room")

class Resource:
    def __init__(self, id, type, status = "available"):
        self.id = id
        self.type = type
        self.status = status

    def needs_resource(self):
        return True

    def __str__(self):
        return f"Resource(id={self.id}, type='{self.type}', status='{self.status}')"

    def __repr__(self):
        return self.__str__()

class Course:
    max_students = 30

    def __init__(self, name):
        self.name = name
        self.current_students = []

    def enroll_student(self, student: 'Student'):
        if len(self.current_students) >= Course.max_students:
            raise ValueError("Course is full.")
        self.current_students.append(student)
    