""" PRINT """
# age = 23
# name= 'Tim'

# print('My name is', name, 'and i am', age, 'years old')

# print('My name is', name, 'and i am', age, 'years old', sep=' --- ')

# print('Hello world', end=' | ')
# print('I am', name)

""" HELP FUNCTION"""
# help(print)

""" RANGE """
# print(list(range(10)))
# print(*list(range(1,12,3)))

""" MAP """
# def addx(x):
#     return x+'21'

strings = ['my', 'world', 'banana', 'apple']
# lengths = map(len, strings)
# print(*list(lengths))
# print(*list(map(addx, strings)))

lengths = map(lambda x: x + ' WOW!', strings)
print(*list(lengths))