#Create a class Student with three subject marks. Add methods for total, percentage, and grade
#(A, B, C, D).
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

    def grade(self):
        if self.percent()>90:
            return "A"
        elif self.percent()>80:
            return "B"
        elif self.percent()>70:
            return "C"
        else:
            return "D"



    def display(self):
        print("Name: ",self.name)
        print("Marks",self.l,self.m,self.n)
        print("Total: ",self.total())
        print("Percent: ",self.percent())
        print("Grade: ",self.grade())


s1=Student("Ayush",5,60,10)
s1.display()