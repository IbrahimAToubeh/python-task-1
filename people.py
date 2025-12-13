from abc import ABC, abstractmethod
from typing import List, Optional
from .mixins import AuditMixin
from .finance import Wallet
from .resources import Course, Resource

class Person(ABC, AuditMixin):
    def __init__(self, name: str, initial_balance: float = 0.0):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name
        self.wallet = Wallet(initial_balance)

    @abstractmethod
    def __str__(self):
        pass
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return False

class Student(Person):
    def __init__(self, name: str, initial_balance: float = 0.0):
        super().__init__(name, initial_balance)
        self.enrolled_courses = []
        self.borrowed_resources = []
        self._progress = 0

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self._progress = value

    def needs_resource(self) -> bool:
        return True

    def enroll(self, course: Course):
        course.enroll_student(self)
        self.enrolled_courses.append(course)
        self.log_action("Enrollment", f"{self.name} enrolled in {course.name}")

    def borrow_resource(self, resource: Resource, mentor: 'Mentor'):
        if mentor.approve_request(self, resource):
            resource.status = "borrowed"
            self.borrowed_resources.append(resource)
            self.log_action("Borrow", f"{self.name} borrowed {resource.id}")
        else:
            self.log_action("Borrow Denied", f"{self.name} denied for {resource.id}")

    def __str__(self):
        return f"Student: {self.name}"

class PremiumStudent(Student):
    def enroll(self, course: Course, mentor: Optional['Mentor'] = None):
        super().enroll(course)
        if mentor:
             self.log_action("Premium Enrollment", f"Matched with mentor {mentor.name}")

class Mentor(Person):
    def approve_request(self, student: Student, resource: Resource) -> bool:
        if resource.status == "available":
            self.log_action("Approval", f"Approved {resource.id} for {student.name}")
            return True
        return False

    def __str__(self):
        return f"Mentor: {self.name}"
