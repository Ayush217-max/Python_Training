
class Payment:
    def __init__(self, balance):
        self.balance = balance
    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Payment successful!")
        else:
            print("Insufficient balance!")

class Googlepay(Payment):
    def pay(self, amount):
        super().pay(amount)

class Phonepay(Payment):
    def pay(self, amount):
        super().pay(amount)

class PayTM(Payment):
    def pay(self, amount):
        super().pay(amount)

print("Welcome to Amazon Payment")
print("Choose a payment method:")
print("1. Google Pay")
print("2. PhonePe")
print("3. PayTM")
choice = input("Enter choice (1/2/3): ")

if choice == '1':
    print("Using Google Pay...")
    amnt = int(input("Enter amount: "))
    Googlepay(1000).pay(amnt)
elif choice == '2':
    print("Using PhonePe...")
    amnt = int(input("Enter amount: "))
    Phonepay(800).pay(amnt)
elif choice == '3':
    print("Using PayTM...")
    amnt = int(input("Enter amount: "))
    PayTM(500).pay(amnt)
else:
    print("Invalid choice!")






