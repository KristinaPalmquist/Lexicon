
"""" OOP 3/3 """

""" POLYMORPHISM """

# # Base class / Parent class / Superclass
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         return f'Some generic sound'

# # Derived class / Child class / Subclass
# class Dog(Animal):
#     def make_sound(self): # own definition, will override superclass def
#         return f'Woof!'

# # Derived class / Child class / Subclass
# class Cat(Animal):
#     def make_sound(self):
#         return 'Meow!'


# animals = [Dog('Buddy'), Cat('Whiskers')]

# for animal in animals:
#     print(f'{animal.name} makes sound: {animal.make_sound()}')


# class Bird:
#     def make_sound(self):
#         return 'Chirp!'

# class Dog:
#     def make_sound(self):
#         return 'Woof!'

# def animal_sound(animal):
#     return animal.make_sound()

# bird = Bird()
# dog = Dog()
# print(animal_sound(bird))
# print(animal_sound(dog))


# class CreditCardPayment:
#     def __init__(self, amount, card_number):
#         self.amount = amount
#         self.card_number = card_number
#     def process_payment(self):
#         print(f'Processing credit card payment of {self.amount} using card number {self.card_number}')

# class PayPalPayment:
#     def __init__(self, amount, paypal_account):
#         self.amount = amount
#         self.paypal_account = paypal_account
#     def process_payment(self):
#         print(f'Processing PayPal payment of {self.amount} from PayPal account {self.paypal_account}')   

# class CryptoPayment:
#     def __init__(self, amount, wallet_address):
#         self.amount = amount
#         self.wallet_address = wallet_address
#     def process_payment(self):
#         print(f'Processing cryptocurrency payment of {self.amount} from account {self.wallet_address}')   
    
# def process_payment(payment):
#     payment.process_payment()

# credit_card = CreditCardPayment(100, '1234-5678-1234-5678')
# paypal = PayPalPayment(200, 'user@example.com')
# crypto = CryptoPayment(0.05, 'abc123xyz456crypto')

# for payment_method in [credit_card, paypal, crypto]:
#     process_payment(payment_method)

""" IMPORTS """

# from math import sqrt
# print(sqrt(25))

# import math
# print(int(math.sqrt(25)))

# from math import sqrt
# import math
# def sqrt(x):
#     return 'hello'
# print(sqrt(25))
# print(math.sqrt(25))

# from math import sqrt as srtq
# print(srtq(25))

# from math import * # avoid, can cause naming polution
# print(sqrt(245))

from demo7_funcs import adder, Dog
print(adder(1,2))


dog = Dog()
print(dog)

# with open('README.md') as file:
    



