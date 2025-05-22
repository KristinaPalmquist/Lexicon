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

# strings = ['my', 'world', 'banana', 'apple']
# lengths = map(len, strings)
# print(*list(lengths))
# print(*list(map(addx, strings)))

# lengths = map(lambda x: x + ' WOW!', strings)
# print(*list(lengths))

""" FILTER """
# strings = ['my', 'world', 'banana', 'aple', 'pear', 'moose', 'mango']
# print(*list(filter(lambda x: x[0] == 'm', strings)))
# print(list(filter(lambda x: len(x) > 4, strings)))

""" SUM """
# numbers = {1, 4.5, 5, 23, 2}
# print(sum(numbers, start = -10))

""" SORTED """
# numbers = {1, 4.5, -2, 5, 0, 23, 2}
# print(sorted(numbers))
# print(sorted(numbers, reverse = True))
# people = [
#     {'name': 'Alcie', "age": 30},
#     {'name': 'Bob', "age": 42},
#     {'name': 'Charlie', "age": 35},
#     {'name': 'Davina', "age": 57},
# ]
# print(sorted(people, key=lambda person: person["age"]))

""" ENUMERATE """
# tasks = ['Write report', 'Attend meeting', 'Review code', 'Submit timesheet']
# # for index in range(len(tasks)):
# #     task = tasks[index]
# #     print(f'{index + 1}. {task}')
# for index, task in enumerate(tasks):
#     print(f'{index + 1}. {task}')
    
""" ZIP """
# names = ['Alice', 'Bob', 'Charlie', 'Davina', 'Engelbert']
# ages = [30, 42, 35, 57]
# print(*list(zip(names, ages)))
# people = []
# for idx in range(min(len(names), len(ages))):
#     people.append((names[idx], ages[idx]))
# print(*list(people))

""" OPEN """
# # path = '/python/concepts/'
# file = open('test.txt', 'w') # read, write, append
# file.write("Hello world\nMy name is Kristina")
# file.close()
# with open('test.txt', 'w') as file: # context manager, will automatically close the file on exit
#     file.write('Hejsan hej\nBanan banan banan\n')
# with open('test.txt', 'a') as file:
#     file.write('Syns det här tro... ?\n')
# with open('test.txt', 'r') as file:
#     print(file.read())