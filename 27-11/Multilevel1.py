
class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print(f"Person: {self.name}")

class Employee(Person):  # Inherits from Person
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_employee(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Manager(Employee):  # Inherits from Employee
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_manager(self):
        print(f"Manager of {self.department}, Name: {self.name}, ID: {self.emp_id}")

# Test
m = Manager("Ayush", 101, "IT")
m.show_person()
m.show_employee()
m.show_manager()
