


""" OOP """

""" OBJECT """

# l = [1,2,3]
# # l.count()
# print(type(l))
# print(type([])) # class 'list'
# print(type(())) # class 'tuple'
# print(type({})) # class 'dict'

# class Sample():
#     # def __init__(self):
#     pass # when you want to leave for later to avoid crash

# x = Sample()
# print(type(x)) # class '__main__.Sample'
        

# class Dog():
#     # class object attributes
#     species = 'mammal'
#     def __init__(self, breed, name): # initializes the attributes of an object
#         self.breed = breed 
#         self.name = name
        
# milo = Dog(breed='Labrador', name='Milo')
# frank = Dog('Huskie', 'Frank')
# print(milo.breed)
# print(milo.species)
# print(frank.breed, frank.name)

# class Circle():
#     pi = 3.14
#     def __init__(self, radius=1):
#         self.radius = radius
    
#     def area(self):
#         return self.radius * self.radius * Circle.pi
   
#     def setRadius(self, radius):
#         self.radius = radius
        
#     def getRadius(self):
#         return self.radius

# c = Circle()
# c.setRadius(2)
# print('Radius is: ', c.getRadius())
# print('Area is: ', c.area())

# class Person:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
        
#     def __str__(self):
#         return f'{self.name} is {self.age} years old and has email {self.email}'
        
# person1 = Person('Rob', 'rob@email.com', 78)
# person2 = Person('Allan', 'allan@email.com', 8)
# print(person1)
# print(person2)

# person1.phone = '070898776'
# print(person1.phone)
# # print(person2.phone) # will cause crash since no phone number added


""" args & kwargs """

# class Person:
#     def __init__(self, **kwargs):
#         self.__dict__=kwargs
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
    
# p1 = Person(name='Alice', age=23)
# p2 = Person(name = 'Bob', age=45)
# # p3 = Person(name='Chuck')

# print(p1)
# print(p2)
# # print(p3)


class Something:
    def __init__(self, data:dict): # type hint
        self.__dict__=data
    def __str__(self):
        str_rep = ''
        ## list comprehension
        for key, value in self.__dict__.items():
            str_rep += f'{key}: {value} '
        
        return str_rep
  
    
data_dict1 = {
    'a': 10,
    'b': 20,
    'name': 'One'
}

data_dict2 = {
    'c': 15,
    'd': 25,
    'name': 'Two'
}
s1 = Something(data_dict1)
s2 = Something(data_dict2)

print(s1)
print(s2)