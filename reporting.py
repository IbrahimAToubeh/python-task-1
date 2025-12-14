from typing import List
from .people import Student, Mentor
from .people import PremiumStudent

class Report:
    def __init__(self, students: int, premium: int, approvals: int, catalog_size: int):
        self.students = students
        self.premium = premium
        self.approvals = approvals
        self.catalog_size = catalog_size

    @classmethod
    def from_students(cls, students: List[Student], mentors: List[Mentor], catalog_size: int):
        total_students = len(students)
        premium_count = sum(1 for s in students if isinstance(s, PremiumStudent))
        approvals = sum(len(s.borrowed_resources) for s in students)
        return cls(total_students, premium_count, approvals, catalog_size)

    @staticmethod
    def format_currency(amount: float) -> str:
        return f"${amount:.2f}"

    def __str__(self):
        return f"REPORT: students={self.students} | premium={self.premium} | mentor_approvals={self.approvals} | catalog_size={self.catalog_size}"
    
    def __add__(self, other):
        if isinstance(other, Report):
            return Report(
                self.students + other.students,
                self.premium + other.premium,
                self.approvals + other.approvals,
                self.catalog_size + other.catalog_size
            )
        return NotImplemented
