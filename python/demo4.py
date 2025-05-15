
""" DEMO 4 """

# """ LAB 3 questions 1-4 """

# """ 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears 
# in the list somewhere. Example: arrayCheck([1, 1, 2, 3, 1]) → True 
# arrayCheck([1, 1, 2, 4, 1]) → False arrayCheck([1, 1, 2, 1, 2, 3]) → True """

# def arrayCheck(nums_list):
#     for i in range(len(nums_list)-2):
#         if nums_list[i] == 1 and nums_list[i+1] == 2 and nums_list[i+2] == 3:
#             return True
#     return False

# test_cases = [
#     [1, 1, 2, 3, 1],
#     [1, 1, 2, 4, 1],
#     [1, 1, 2, 1, 2, 3],
# ]

# results = [arrayCheck(case) for case in test_cases ]
# print(results)

# """ 2. Given a string, return a new string made of every other character starting with 
# the first, so "Hello" yields "Hlo". Example: stringBits('Hello') → 'Hlo' 
# stringBits('Hi') → 'H' stringBits('Heeololeo') → 'Hello' """
# def stringBits(string):
#     return string[::2] # slice notation

# test_strings = [ 'Hello', 'Hi', 'Heeololeo',]

# res = [stringBits(case) for case in test_strings ]
# print(res)
 
# """ 3. Given a string, return a string where for every char in the original, # there are two chars.
# doubleChar('The') → 'TThhee' doubleChar('AAbb') → 'AAAAbbbb' doubleChar('Hi-There') → 'HHii--TThheerree' """
# def doubleChar(my_string):
#     return ''.join([char*2 for char in my_string])

# test_chars = ['The', 'AAbb', 'Hi-There',]

# result = [doubleChar(case) for case in test_chars ]
# print(result)

# """ 4. Return the number of even integers in the given array/list. Examples:
# count_evens([2, 1, 2, 3, 4]) → 3 count_evens([2, 2, 0]) → 3 count_evens([1, 3, 5]) → 0 """
# def count_evens(nums):
#     return sum(1 for num in nums if num %2 == 0)

# test_lists = [[2, 1, 2, 3, 4], [2, 2, 0], [1, 3, 5],]

# res_number = [count_evens(case) for case in test_lists ]
# print(res_number)

""" LAMBDA """

# def timesTwo(num): # function version
#     return num*2

# print(timesTwo(8))

# lambda num: num*2 # lambda input functionality

""" FILTER """
# lst = [1,2, 3,4,5 ,6, 7, 8, 9,10]

# def evenBool(num):
#     return num%2 == 0 

# evens = filter(evenBool, lst)
# print(list(evens))

# evens = filter(lambda num: num%2 == 0, lst)
# print(list(evens))

# values = [1,2,3,4,5]

# answer = map(lambda x: x+1, values)
# print(list(answer))

# def mapper(helper_func, iterable):
#     result = []
#     for value in iterable:
#         helper_result = helper_func(value)
#         result.append(helper_result)
#     return result

# values = [1,2,3,4,5]
# result = mapper(lambda x: x-1, values)

# print(list(result))

""" SCOPE """

# x = 15

# def printer():
#     x = 30
#     return x

# print(x)
# print(printer())
# print(x)

# """ Local """
# f = lambda x: x**2
# """ Enclosing function """
# name = 'This is some global name'
# def greet():
#     name = 'Erik'
#     def hello():
#         print('Hello ' + name)
#     hello()
# greet()
# print(name)

# """ Global """
# print(obj: Sized, /) -> int

# """ Built-in """
# len()

# x = 50

# def func(x):
#     print('x is', x)
#     x = 2
#     print('change local x to', x)
    
# func(x)
# print('x is still', x)

# x = 50

# def func():
#    global x
#    print('This is the global x:', x)
#    x = 2
#    print('Ran func, which changed global x to', x)

# print('first value for x:', x)
# func()
# print('x is now', x)

li = [lambda arg=x: arg * 10 for x in range(1,5)]
for i in li:
    print(i())

