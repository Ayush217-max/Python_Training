#Create a class Customer with attributes name, age, city. Add a method that checks if the
#customer is eligible for a loyalty program (age &gt; 25).

class Customer():
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def elligible(self):
        if self.age>25:
            print("YES")
        else:
            print("NO")

c=Customer("Ayush",21,"Kochi")
c.elligible()
