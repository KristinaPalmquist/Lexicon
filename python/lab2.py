"""
1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
"""
print('\n1. POWER OF -------------------------------------------------------')
base = int(input('What number do you want to use as the base? '))
exponent = int(input('What number do you want to use as the exponent? '))
power = base**exponent
print(f'{base} to the power of {exponent} is {power}')

"""
 2. Write a program that calculates the sum of all elements in a given tuple.
"""
print('\n2. SUM OF TUPLE ---------------------------------------------------')
my_tuple = (1,5,7,8,2,4,6,7,3)
print(sum(my_tuple))

"""
 3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
"""
print('\n3. TUPLE OF EVEN INTS ---------------------------------------------')

int_tuple = (1,5,7,8,2,4,6,7,3)
print(tuple(int for int in int_tuple if int%2 == 0)) 
 
"""
 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
"""
print('\n4. MERGE DICTIONARIES ---------------------------------------------')

dictionary1 = {
    'key1': 1,
    'key2': 2,
    'key3': 108,
    'key7': 7
}
dictionary2 = {
    'key1': 67,
    'key2': 56,
    'key4': 93,
    'key7': 33   
}
new_dictionary = dictionary2 | dictionary1
print(new_dictionary)

"""
 5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
"""
print('\n5. LIST COMPREHENSION ----------------------------------------------')
int_list = [3,45,65,2,7,9,67,88,4]
print([item for item in int_list if item%2 == 0])

"""
6. Write a program that takes a string as input and prints its reverse.
"""
print('\n6. BACKWARDS ------------------------------------------------------')
my_str = 'Hej Lexicon!'
print(my_str[::-1])

""" 
7. You are given a list called mypairs. This list contains several tuples, and each tuple holds exactly 10 integers.
Your task is to write two different solutions that print out each individual value inside the tuples:
Manual unpacking – Do it like we did in class: unpack all 10 values into individual variables in the for-loop.
Smarter unpacking – Write an alternative solution that achieves the same result, but in a more flexible or elegant way (e.g. a solution that would still work if the number of values changes in the future).
"""
print('\n7. UNPACKING TUPLES ----------------------------------------------')
mypairs = [
    (3,4,6,7,8,9,10,11,34, 13), 
    (5,6,7,8,1,2,13,24,465,3), 
    (34,5,6,7,8,13,24,21,7,1)
    ]
        
print('\nLESSON')
for one, two, three, four, five, six, seven, eight, nine, ten in mypairs:
    print(one, two, three, four, five, six, seven, eight, nine, ten)

print('\nMY SOLUTION')
for tup in mypairs:
    for val in tup:
        print(val, end=' ')
    print('')



