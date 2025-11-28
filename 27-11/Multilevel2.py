
class Device:
    def __init__(self, brand):
        self.brand = brand

    def show_device(self):
        print(f"Device Brand: {self.brand}")

class Computer(Device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor

    def show_computer(self):
        print(f"Computer: {self.brand}, Processor: {self.processor}")

class Laptop(Computer):
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)
        self.battery_life = battery_life

    def show_laptop(self):
        print(f"Laptop: {self.brand}, Processor: {self.processor}, Battery: {self.battery_life} hrs")

# Test
l = Laptop("Dell", "i7", 8)
l.show_device()
l.show_computer()
l.show_laptop()
