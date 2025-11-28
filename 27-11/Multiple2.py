
class ElectricVehicle:
    def charge_battery(self):
        print("Battery charging...")

class FuelVehicle:
    def refuel(self):
        print("Refueling with petrol...")

class HybridCar(ElectricVehicle, FuelVehicle):
    def drive(self):
        print("Driving in hybrid mode...")

# Usage
hc = HybridCar()
hc.charge_battery()  # From ElectricVehicle
hc.refuel()          # From FuelVehicle
hc.drive() 