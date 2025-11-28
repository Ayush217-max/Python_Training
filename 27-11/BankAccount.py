
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Balance: {self.balance}")

class SavingsAccount(BankAccount):  # Single inheritance
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}, New Balance: {self.balance}")

# Test
s = SavingsAccount(1000, 5)
s.deposit(500)
s.add_interest()
