

""" LAB 7 """
""" Exercise 1 Polymorphism
Create a Python program that explores polymorphism using a hierarchy of shapes. Start with 
a base class Shape, and then create two or more derived classes (e.g., Circle, Rectangle, 
Triangle) that inherit from the Shape class. Each shape class should have its own 
implementation of methods like area() and perimeter(). These methods will calculate the 
area and perimeter of the respective shape."""
"""1. Define the Shape base class with methods like area() and perimeter(). You can 
initialize any common attributes in the base class."""
"""2. Create derived classes for di􏰀erent shapes, e.g., Circle, Rectangle, and Triangle. Each 
derived class should inherit from the Shape base class and implement its own version of 
the area() and perimeter() methods."""
"""3. Implement specific methods for each derived class. For example, the Circle class might 
have a method to calculate its area based on the radius, and the Rectangle class could have 
a method to calculate its area based on length and width.
Create instances of each shape type and demonstrate the use of polymorphism by calling the 
area() and perimeter() methods on them."""
from math import pi, sqrt

class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return f'Area calc not defined'
    def perimeter(self):
        return f'No perimeter calculation defined'
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(height=radius*2, width=radius*2)
        self.radius = radius
    def area(self):
        return pi * self.radius**2 
    def perimeter(self):
        return 2 * pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return self.height * 2 + self.width * 2
    
class Triangle(Shape):
    def __init__(self, side_A, side_B, side_C):
        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C        
    def area(self):
        sp = (self.side_A + self.side_B + self.side_C)/2
        return sqrt(sp * (sp-self.side_A) * (sp-self.side_B) * (sp-self.side_C))
    def perimeter(self):
        return self.side_A + self.side_B + self.side_C
    
circle = Circle(10)
triangle = Triangle(3,4,5)
rectangle = Rectangle(3,4)
print(f'Circle - Area: {round(circle.area(), 2)} / Perimeter: {round(circle.perimeter(), 2)}')
print(f'Triangle - Area: {round(triangle.area(), 2)} / Perimeter: {triangle.perimeter()}')
print(f'Rectangle - Area: {rectangle.area()} / Perimeter: {rectangle.perimeter()}')

"""Exercise 2
Implement a Plugin System Using Duck Typing
Create classes UpperCaseFormatter, LowerCaseFormatter, and TitleCaseFormatter that 
implement a format_text(text) method."""
"""Write a function apply_formatters(text, formatters) that applies a list of formatters to 
a string."""
"""Bonus:
Add error handling to check if objects passed to apply_formatters actually have a 
format_text() method, raising a custom FormatterError if not. """

class UpperCaseFormatter:
    def format_text(self, text):
        return f'{text.upper()}'

class LowerCaseFormatter:
    def format_text(self, text):
        return f'{text.lower()}'
    
class TitleCaseFormatter:
    def format_text(self, text):
        return f'{text.title()}'
    
class FawltyFormatter:
    pass
    
class FormatterError(Exception):
    def __init__(self, formatter):
        self.formatter_name = formatter.__class__.__name__
        self.message = f"{self.formatter_name} does not have a 'format_text' method"
        super().__init__(self.message)
    def __str__(self):
        return self.message
    
def apply_formatters(text, formatters):
    formatted_texts = []
    for formatter in formatters:
        try:
            if not hasattr(formatter, 'format_text') or not callable(formatter.format_text):
                raise FormatterError(formatter)
            formatted_texts.append(formatter.format_text(text))
        except FormatterError as e:
            print(f"Error: {e}")
    return formatted_texts
    

print(*apply_formatters('lexiCon IT proFFs', [UpperCaseFormatter(), LowerCaseFormatter(), TitleCaseFormatter()]), sep='\n')
