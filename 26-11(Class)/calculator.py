class Calculator:

    def add(self,a,b):
        print("Result:",a+b)

    def sub(self,a,b):
        if a>b:
            print("Result:",a-b)
        else:
            print("Result:",b-a)

    def mul(self,a,b):
        print("Result:",a*b)

    def div(self,a,b):
        try:
            print("Result:",a/b)
        except ZeroDivisionError:
            print("cant divide by zero")

c1=Calculator()
c1.add(1,2)
c1.sub(3,4)
c1.mul(5,6)
c1.div(3,0)