
""" Todays Lab 2025-05-14
In this lab, we will create a Python program to model a basic student database using OOP concepts.
1. Define a Student Class:
 	Define a class named Student with the following attributes:
 		- name: Name of the student (string).
 		- age: Age of the student (int).
 		- grade: Grade level of the student (int).
2. Add Methods:
 	Add the following methods to the Student class:
 		- get_info( ): Method to display the student's information.
 		- promote ( ): Method to promote the student to the next grade level.
3. Test the Class:
 	Create instances of the Student class and test its methods:
 		- Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
 		- Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information. """
   
class Student:
    def __init__(self, name:str, age:int, grade:int):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f'Student: {self.name}, {self.age}, grade: {self.grade}'
    def get_info(self):
        print(('NAME:').ljust(20), ('AGE:').center(5), ('GRADE:').center(10))
        print(self.name.ljust(20), str(self.age).center(5), str(self.grade).center(10))
    def promote(self):
        self.grade +=1
        

stud1 = Student(name='Anna', age=15, grade=9)
stud2 = Student(name='Bob', age=21, grade=4)
stud1.get_info()
stud1.promote()
stud1.get_info()

""" rewrite with list comprehension """
class Something:
    def __init__(self, data:dict): # type hint
        self.__dict__=data
    def __str__(self):
        str_rep = ', '.join([( f'{key}: {value} ') for key, value in self.__dict__.items()])
        return str_rep


s1 = Something({'a': 10, 'b': 20, 'name': 'One'})
s2 = Something({'c': 15, 'd': 25, 'name': 'Two'})

print(s1)
print(s2)