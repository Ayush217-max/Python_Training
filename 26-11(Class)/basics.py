class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print(self.brand)
        print(self.model)
        print(self.price)


# creating three car objects
car1 = Car("Toyota","fortuner",5000000)
car2 = Car("mercedes","a5",8000000)
car3 = Car("Tesla","model 3",60000000)

# Display

car1.display()
print()
car2.display()
print()
car3.display()

