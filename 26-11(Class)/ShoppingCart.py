class ShopingCart:
    def __init__(self):
        self.items = []
    def addItem(self,name,price):
        self.items.append((name,price))
        print(name,"added to cart")

    def removeItem(self,name):
        for i in self.items:
            if i[0] == name:
                self.items.remove(i)
                print(name, "removed from cart")
                return
        print("item not found in cart")

    def total_cost(self):
        t=0
        for i in self.items:
            t += i[1]
        return t

    def apply_discount(self,p):
        t= self.total_cost()
        dp = t*(p/100)
        fp=t-dp
        return fp

    def display(self):
        if not self.items:
            print("No items in the cart")
            return
        print("Items in cart:")
        for n,m in self.items:
            print(n,"-",m)


c=ShopingCart()
c.addItem("lap",50000)
c.addItem("mobile",20000)
c.addItem("mouse",5000)

print()
c.display()
print()

print("Total cost:",c.total_cost())
print("Final price after discount:",c.apply_discount(10))

print()
c.removeItem("lap")
c.display()

