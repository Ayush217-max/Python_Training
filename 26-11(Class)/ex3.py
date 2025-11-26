#Create a class BankAccount that supports deposit, withdraw, check balance, and displays
#transaction logs.
class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.log=[]


    def deposit(self,amount):
        self.balance=self.balance+amount
        self.log.append(f'Deposited {amount} the current balance is {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print("you cannot withdraw more than you have")
        else:
            self.balance=self.balance-amount
            self.log.append(f'Withdrawn {amount} the current balance is {self.balance}')

    def checkbalance(self):
        print(self.balance)

    def display(self):
        print(self.name)
        print(self.balance)
        for l in self.log:
            print(l)

a1=BankAccount("Ayush",50000)
a1.deposit(5000)
a1.withdraw(50000)
a1.withdraw(50000)
a1.checkbalance()
a1.display()



