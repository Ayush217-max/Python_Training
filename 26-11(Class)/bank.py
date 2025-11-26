class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("you cannot withdraw more than you have")
        else:
            self.balance=self.balance-amount

    def display(self):
        print(self.name)
        print(self.balance)

a1=Account("Ayush",50000)
a1.deposit(5000)
a1.withdraw(50000)
a1.withdraw(50000)
a1.display()



