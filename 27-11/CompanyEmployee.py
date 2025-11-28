
class Company:
    def __init__(self, name):
        self.name = name

    def show_company(self):
        print(f"Company: {self.name}")

class Employee(Company):  # Single inheritance
    def __init__(self, name, emp_name):
        super().__init__(name)  # Call parent constructor
        self.emp_name = emp_name

    def show_employee(self):
        print(f"Employee: {self.emp_name}, Company: {self.name}")

# Test
e = Employee("TechCorp", "Ayush")
e.show_company()
e.show_employee()
