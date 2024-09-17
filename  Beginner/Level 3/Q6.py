# Single Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        print(f"This is a {self.make} {self.model} vehicle.")

# Parent Class inheriting from Vehicle (Multilevel Inheritance)
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def description(self):
        print(f"This is a {self.make} {self.model} car that runs on {self.fuel_type}.")

# Parent Class for Multiple Inheritance
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"This vehicle has a {self.battery_capacity} kWh battery.")

# Multiple Inheritance: Child Class inheriting from both Car and Electric
class ElectricCar(Car, Electric):
    def __init__(self, make, model, fuel_type, battery_capacity):
        Car.__init__(self, make, model, fuel_type)
        Electric.__init__(self, battery_capacity)

    def description(self):
        print(f"This is a {self.make} {self.model} electric car with a {self.battery_capacity} kWh battery.")

# Multilevel Inheritance: Child Class inheriting from Car
class SportsCar(Car):
    def __init__(self, make, model, fuel_type, top_speed):
        super().__init__(make, model, fuel_type)
        self.top_speed = top_speed

    def description(self):
        print(f"This is a {self.make} {self.model} sports car with a top speed of {self.top_speed} km/h.")

# Single Inheritance
print("Single Inheritance:")
vehicle = Vehicle("Honda", "City")
vehicle.description()  

# Multilevel Inheritance
print("\nMultilevel Inheritance:")
sports_car = SportsCar("Ferrari", "488 GTB", "petrol", 330)
sports_car.description()  

# Multiple Inheritance
print("\nMultiple Inheritance:")
e_car = ElectricCar("Tesla", "Model 3", "electric", 120)
e_car.description()  
e_car.battery_info() 
