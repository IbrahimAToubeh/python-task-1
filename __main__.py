from .people import Student, PremiumStudent, Mentor
from .resources import Course, Resource
from .catalog import ResourceCatalog
from .reporting import Report

def run_demo():
    print("--- Campus Resource Hub Demo ---")
    
    zahra = Student("Zahra", initial_balance=500.0)
    malik = PremiumStudent("Malik", initial_balance=1000.0)
    omar = Mentor("Omar")
    
    python_course = Course("Async Python")
    web_course = Course("Web Development")
    data_course = Course("Data Science")
    
    res1 = Resource("R-001", "Laptop")
    res2 = Resource("R-002", "Book")
    res3 = Resource("R-003", "Room")
    
    catalog = ResourceCatalog()
    catalog.add_resource(res1)
    catalog.add_resource(res2)
    catalog.add_resource(res3)

    zahra.enroll(python_course)
    malik.enroll(web_course, mentor=omar)

    print("\n--- Wallet Transfers ---")
    print(f"Zahra before: {zahra.wallet.balance}")
    print(f"Malik before: {malik.wallet.balance}")
    zahra.wallet.transfer(malik.wallet, 150.0)
    print(f"Zahra after: {zahra.wallet.balance}")
    print(f"Malik after: {malik.wallet.balance}")

    print("\n--- Resource Borrowing ---")
    zahra.borrow_resource(res3, omar)
    malik.borrow_resource(res1, omar)

    print("\n--- Catalog Allocation ---")
    catalog.allocate(zahra, "Laptop")
    catalog.allocate(malik, "Room")

    print("\n--- Catalog ---")
    for res in catalog:
        print(res)

    print("\n--- Final Report ---")
    report = Report.from_students([zahra, malik], [omar], len(catalog))
    print(report)

if __name__ == "__main__":
    run_demo()
