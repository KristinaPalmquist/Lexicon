

""" LAB 2 """
# # write a program that takes two integeres as input, base and exponent, and calculates
# # the power using loops

# base = int(input('Enter the base: '))
# exponent = int(input('Enter the exponent: '))
# result = 1

# for _ in range(exponent): # underscore for variable that is not used
#    # result = result * base
#    result *= base # augmented assignment

# print('If base = {} and exponent = {}. Then result is {}'.format(base, exponent, result))

# # print(f"{base} to the power of {exponent} is {result}")

# # the loop does not work if exponent is a negative number
# 

""" FUNCTIONS """
# a = 1
# b = 4

# def sum(c, d):
#     return c + d

# print(sum(a, b))

# def any_name(parameter='default'):
#     """
#     docstring, explain this function does this and that
#     """
#     print(parameter)
    
# any_name()

# def hello():
#     print('hello')
    
# hello()

# def giveMeHello():
#     return 'Hello you!'

# res = giveMeHello()
# print(res)

# def evenCheck(number):
#     # if number%2 == 0:
#     #     return 'Even'
#     # else:
#     #     return 'Odd'
#     return number % 2 == 0
    
# print(evenCheck(1))
# print(evenCheck(2))
# print(evenCheck(3))
# print(evenCheck(4))
# print(evenCheck(5))
# print(evenCheck(6))
# print(evenCheck(7))


""" default value """
# def helloYou(name='Haithem'):
#     print('Hello', name)


# helloYou('Anna')
# helloYou()


# def addEvenOnly(num1, num2):
#     if num1 %2 != 0 or num2 % 2 != 0:
#         return False
#     return num1 + num2

# print(addEvenOnly(24, 68))
# print(addEvenOnly(65, 68))
# print(addEvenOnly(24, 2))
# print(addEvenOnly(24, 78))


# def func(a,b,c = 10,d = 11):
#     print(a,b,c,d)
    
# func(1,2)
# func(1,2,3)
# func(1,2,3,4)
# func(1,2,d=4)    
# func(c='c', a='a', b='b')
# func(c='c', a='a', d='d', b='b')
    
""" ARGS """
# def func(*args): # pass any number of arguments => tuple, immutable sequence
#     print(args)
    
# func()
# func(1)
# func(1,2)
# func(1,2,3)

""" KWARGS """
# def func2(a, b , **kwargs): # key word argumnents
#     print(a, b)
#     print(kwargs)

# func2(1,2)
# func2(2,3, c=14, d=19)

# def func2(a, b , **kwargs): # key word argumnents
#     print(a, b, kwargs['c'], kwargs['d'])

# func2(2,3, c=14, d=19)

# def func2(a, b , **kwargs): # key word argumnents
#     print(a,b)
#     if 'c' in kwargs:
#         print(kwargs['c'])
#     if 'd' in kwargs:
#         print(kwargs['d'])

# func2(1,2)
# func2(2,3, c=14)
# func2(2,3, c=14, d=19)

# example
def func3(a,b, *args, name='Haithem', **kwargs):
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('args = {}'.format(args))
    print('name = {}'.format(name))
    print('kwargs = {}'.format(kwargs))
    
func3(1,2)
func3(1,2,3,4, name='Anna', age='34', email='anna@email.com')
func3(1,2,3,4,'Anna', age='34', email='anna@email.com')