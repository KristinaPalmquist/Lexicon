

""" Day 6 """

""" DUNDER METHODS - ADD ON TO DEMO 5 """

# point in two dimensional world (x, y)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __repr__(self): # dunder method 
#         return f'Point(x={self.x}, y={self.y})'
    
#     def __str__(self): # default choice for printing the object
#         return f'Point object with (x={self.x}, y={self.y})'
    
# point1 = Point(x=10, y=20)
# print(point1.x, point1.y)
# print(point1)
# print(repr(point1))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
    
# point1 = Point(x=10, y=20)
# point2 = Point(x=10, y=20)
# print(point1)
# print(point2)
# print(point1 == point2) # will use __eq__ if exists
# print(point1.x == point2.x)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def swap_xy(self):
#         self.x, self.y = self.y, self.x
    
    
# point1 = Point(x=10, y=20)
# print(point1.x, point1.y)
# point1.swap_xy()
# print(point1.x, point1.y)


""" INHERITANCE """

# class A:
#     def __init__(self, value):
#         print(f'In A.__init__ and value {value}')
#         self.value = value


# class B(A): # put the class to inherit from
#     def __init__(self, value):
#         print(f'In B.__init__ and value {value}')
#         self.value = value


# b = B(21) # prints from A if no __init__ method in B
# print(b.value) # prints value in B

""" MULTIPLE INHERITANCE"""

# class A:
#     def __init__(self, value):
#         print(f'In A.__init__ and value {value}')
#         self.value = value

# class B(A): # put the class to inherit from
#     def __init__(self, value):
#         print(f'In B.__init__ and value {value}')
#         self.value = value
#         super().__init__(value)
#         self.value += 10

# class C(A):
#     def __init__(self, value):
#         print(f'In C.__init__ and value {value}')
#         super().__init__(value)
#         self.value *= 4
        
# class D(C, B): # multiple inheritance
#     def __init__(self, value):
#         print(f'In D.__init__ and value {value}')
#         super().__init__(value)

# d = D(10)
# print(d.value)
""" MRO """
# print(D.mro())

# class Animal: # base class
#     def __init__(self):
#         print('Animal created')
#     def whoAmI(self): # only if unique
#         print('Animal')
#     def eat(self): # Dog will inherit
#         print('Eating... nom nom')
    
# class Dog(Animal): # derived class
#     def __init__(self):
#         # super().__init__() # if added both init-methods will run
#         print('Dog created')
#     def whoAmI(self): # overrides
#         print('Dog')
#     def bark(self): # unique method
#         print('Woof')

# puppy = Dog()
# puppy.whoAmI()
# puppy.eat()
# puppy.bark()


class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def __str__(self):
        name = (self.first_name + ' ' + self.last_name).ljust(24)
        return name + f' earns {self.salary}'
       # return f'{self.first_name} {self.last_name} earns {self.salary}'
    def increase_salary(self):
        self.salary = int(self.salary * self.increase)

class Developer(Employee):
    increase = 1.10
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang
    def __str__(self):
        return f'{super().__str__()} - {self.prog_lang} Developer'

emp1 = Employee('Alice', 'Abrahamsson', 45000)
emp2 = Employee('Bob', 'Bernhard', 42000)
dev1 = Developer('Carl', 'Ceder', 50000, 'Python')

print(emp1)
print(emp2)
print(dev1)
emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()
print(emp1)
print(emp2)
print(dev1)





