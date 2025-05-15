
""" LAB 6 """

"""1. Veichle Inheritance
Create a Python program that models a hierarchy of vehicles using inheritance. Start with a base 
class Vehicle, and then create two or more derived classes (e.g., Car, Bicycle, Motorcycle) that
inherit from the Vehicle class. Each class should have specific attributes and methods related to
the type of vehicle it represents."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print('Starting vehicle')
    def stop(self):
        print('Vehicle stopped')
    def fuel_up(self):
        print('Needs fuel')
        
    
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        self.num_doors = num_doors
        self.fuel_type = fuel_type
        super().__init__(make, model, year)
    def honk_horn(self):
        print("Beep beep!")
    def open_trunk(self):
        print("Trunk is now open.")
    def lock_doors(self):
        print("Doors are locked.")
        
class Bicycle(Vehicle):
    gear = 0
    def __init__(self, make, model, year, num_gears, type, has_basket):
        self.num_gears = num_gears
        self.type = type
        self.has_basket = has_basket
        super().__init__(make, model, year)
    def ring_bell(self):
        print("Ring ring!")
    def change_gear(self, gear): 
        if gear < self.num_gears:
            self.gear = gear
            print(f"Gear changed to {gear}.")
    def attach_basket(self):
        self.has_basket = True
        print("Basket attached to the bicycle.")
    def detach_basket(self):
        self.has_basket = False
        print("Basket removed from the bicycle.")
    def make_sound(self):
        print('Woosh!')

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        self.type = type
        super().__init__(make, model, year)
    def honk_horn(self):
        print("Honk!")
    def make_sound(self):
        print('Vroom vroom!')

car = Car("Toyota", "Camry", 2020, 4, "Petrol")
bicycle = Bicycle("Giant", "Escape 3", 2021, 21, "Hybrid", True)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

car.start()
car.honk_horn()
car.open_trunk()

bicycle.start()
bicycle.ring_bell()
bicycle.change_gear(5)
print(bicycle.gear)

motorcycle.start()
motorcycle.make_sound()


"""1.1. Define the Vehicle base class with common attributes such as make, model, and year, and 
methods like start(), stop(), and fuel_up()."""
"""1.2. Create derived classes for di􏰀erent types of vehicles, e.g., Car, Bicycle, and Motorcycle. 
Each derived class should inherit from the Vehicle base class and add attributes and methods
specific to that type of vehicle. For example, the Car class might have attributes like num_doors,
and the Bicycle class could have attributes like num_gears."""
"""1.3. Implement specific methods for each derived class. For instance, the Car class might have a
method to honk the horn, and the Bicycle class could have a method to ring the bell."""
"""1.4. Create instances of each vehicle type and demonstrate their specific methods and 
attributes. For example, you can create a car, bicycle, and motorcycle, and call methods like start
(), stop(), and their specific methods like honk_horn() or ring_bell()."""

"""2. Multiple Inheritance and MRO Challenge. Task:
2.1. Create classes X, Y, Z, each with an identify() method.
2.2. Create a class W that inherits from both X and Y.
2.3. Call the identify() method on an instance of W and print the MRO of W."""
"""Challenge:
2.4. Add a super() call in one of the subclasses identify() methods to observe how the method 
chaining works."""

class X:
    def identify(self):
        print(f'X identified')
        
class Y:
    def identify(self):
        print(f'Y identified')

class Z:
    def identify(self):
        print(f'Z identified')

# class W(X, Y):
#     def identify(self):
#         return super().identify()
    
class W(Y, X):
    def identify(self):
        return super().identify()
    
w = W()
w.identify()
print(W.mro())