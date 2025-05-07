# a = 2
# print(type(a))

# income = 100
# tax_rate = 0.3
# taxes = income * tax_rate
# print(taxes)

# h = 'hello'
# print(h[-1])

# print("Hello \nWorld")
# print(len('Hello world'))

# a = 'Hello World'
# print(a[:3])
# print(a[:-1])
# print(a[::2])


# # a[10] = '!' # string immutability
# a = a + '!'
# print(a)
# letter = 'z'
# print(letter*10)

# # object.method(parameters)
# print(a.upper())
# print(a.lower())
# print(a.split())

# print(a.split('o'))



# print('This is a string with an {p}'.format(p = 'insert'))

# print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi'))

# print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a='Rut', b = 'Harry', c = 'Peter'))

# a='Rut'
# b = 'Harry'
# c = 'Peter'
# print(f'Object 1: {a}, Object 2: {b}, Object 3: {c}')

# my_list = [a, 1, 'A string', 23, 100.242, 'a']
# print(my_list)

# print(len(my_list))

# print(my_list[:3])

# print(my_list + ['new item'])
# print(my_list)
# my_list.append('new item')
# print(my_list)
# my_list += ['new item']
# print(my_list)

# new_list = [1,2,3,7,8,1,2,3]
# new_list.sort()
# print(new_list)

# popped_item = new_list.pop(3) # index
# print(new_list)
# print(popped_item)

# if len(new_list) > 10:
#     print(new_list[10])
# else:
#     print('No index 10')
    
# new_list = ['a', 'j', 'r', 's', 'c']
# new_list.reverse()
# print(new_list)
# new_list.sort()
# print(new_list)

# new_list.remove('r')
# print(new_list)

# new_list.pop()
# print(new_list)

# new_list.remove('r')
# print(new_list)

# list_1 = [1,2,3]
# list_2 = [4,5,6]
# list_3 = [7,8,9]
# matrix = [list_1, list_2, list_3]
# # print(matrix)

# # print(matrix[1])
# # print(matrix[0][0])

# # for i in matrix:
# #     for j in i:
# #         print(j)

# # first_column = [row[0] for row in matrix] # list comprehension
# # print(first_column)

# # first_column = [row[0]*2 for row in matrix] # list comprehension
# # print(first_column)

# doubled_matrix = [[element * 2 for element in row] for row in matrix]
# print(doubled_matrix)


# dictionaries
# my_dictionary = {
#     1: 'value one',
#     2: 'value two',
#     3: 'value three'
# }
# print(my_dictionary[1], my_dictionary[2], my_dictionary[3])

# my_dictionary = {
#     'one': 'value one',
#     'two': 'value two',
#     3: 'value three',
#     4: ['name one', 'name_two']
# }
# print(
#     my_dictionary['one'], my_dictionary[3], 
#     my_dictionary[4], my_dictionary[4][0])

# print(my_dictionary[4][1].upper())

# my_dictionary[4][1] = my_dictionary[4][1].upper()
# my_dictionary['one'] = 'Updated New Value'
# my_dictionary[4] += ['name_three']

# print(my_dictionary)

# new_dictionary = {}
# new_dictionary['animal'] = 'cat'
# new_dictionary['age'] = 21
# new_dictionary['answer'] = True
# new_dictionary['another'] = {'three': 8}

# print(new_dictionary)

nested_dictionary = {
    'person1': {
        'name': {'first': 'Alice', 'last': 'Andersson'},
        'age': 37
    },
    'person2': {
        'name': {'first':'Bob', 'last': 'Bobivarian'},
        'age': 22
    }
}

# print(nested_dictionary)
# print(nested_dictionary['person1'])

# print(nested_dictionary['person1']['name']['first'])
# print(nested_dictionary['person2']['name'])
# for person in nested_dictionary:
#         print(person)


# dictionary = {
#     'key1': 1,
#     'key2': 2,
#     'key3': 3
# }

# # print(dictionary.keys())
# # print(dictionary.values())
# print(dictionary.items()) # separates into tuples



