
class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def manage(self):
        print("Managing team")

class Developer(Employee):
    def code(self):
        print("Writing code")

class Tester(Employee):
    def test(self):
        print("Testing software")

# Usage
m = Manager()
m.work()    # From Employee
m.manage()  # From Manager
