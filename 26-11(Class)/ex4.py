#Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage.
class Mobile:
    def __init__(self,name,model,storage):
        self.name = name
        self.model = model
        self.storage = storage
    def upgrade(self):
        self.storage = self.storage+15
    def display(self):
        print("Name:",self.name)
        print("Model:",self.model)
        print("Storage:",self.storage,"GB")

m=Mobile("iphone",16,256)
m.display()
m.upgrade()
m.display()