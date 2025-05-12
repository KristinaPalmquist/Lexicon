s = 'Python'

print('1: ---')
print(s[4])
print(s[:4]) # string slicing
print(s[1:4])
print(s[::-1])

print()
print('2: ---')
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

print()
print('3: ---')
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {
    'k1': [{
            'nest_key': ['this is deep', ['hello']]
            }]
    }
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

print()
print('4: ---')
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
myset = list(set(mylist))
print(myset)

print()
print('5: ---')
age = 4
name = 'Sammy'
print(f"Hello my dog's name is {name} and he is {age} years old")
print("Hello my dog's name is {} and he is {} years old".format(name, age))