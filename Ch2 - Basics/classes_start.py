#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self) -> None:
            self.make = "Unknown"
            self.model = "Unknown Model"
            self.year = 0
    
    def display_details(self):
        print(f"\nMake: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}\n")
        

my_car = Vehicle()
my_truck = Vehicle()

my_car.make = "Toyota"
my_car.model = "Camry"
my_car.year = 2018

my_truck.make = "Ford"
my_truck.model = "F-150"
my_truck.year = 2019

print("Car Details:\n")
my_car.display_details()

print("\nTruck Details:\n")
my_truck.display_details()