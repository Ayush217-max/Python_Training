class Student:
    def __init__(self,name,l,m,n):
        self.name = name
        self.l = l
        self.m = m
        self.n = n

    def total(self):
        return self.l+self.m+self.n

    def percent(self):
        return (self.total()/300)*100

    def display(self):
        print("Name: ",self.name)
        print("Marks",self.l,self.m,self.n)
        print("Total: ",self.total())
        print("Percent: ",self.percent())


s1=Student("Ayush",5,60,10)
s1.display()