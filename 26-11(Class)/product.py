#Create a class Product with attributes name, price, quantity. Add a method to calculate the
#total cost of all quantities.

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        self.cost = (self.price * self.quantity)
        return self.cost

    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Cost:",self.calculate())


p=Product("lap",70000,3)
p.display()