""" LAB 4 """
"""1.Write a lambda function to calculate the square of a number."""
y = lambda x: x * x
print('1:', y(5))

""" 2.Write a function that takes a list of numbers and returns a 
list containing the squares of each number using lambda."""
nums = [1,3,5,7,9,0]
list_square = map(lambda num: num * num, nums)
print('2:', list(list_square))

""" 3.Write a function that returns a list of prime numbers up to 
a given number using lambda."""
def list_prime(length):
    primes = list( # cast the resulting object as a list
        filter( # takes a function and a list as arguments
        lambda num: # check if each num is prime
            num > 1 and # start from 2 - 0 and 1 are not prime
            all( # check all elements in iterable are True, (num has to be not divisible by any i)
                num % i != 0 # check that num is not divisable by i
                for i in 
                range(2, int(num ** 0.5) + 1)), # set range from 2 to the square root of num (incl)
        range(length + 1))) # to include the length number 
    return primes

print('3:', list_prime(20))

""" 4. Write a program that modifies a global variable inside a function """
name = 'Herbert'
def update_name(new_name):
    global name
    name = new_name
print('4:', 'Name before function is run:', name)
update_name('Anna')
print('  ', 'Name after function is run:', name)

""" 5. Create a program that defines a function within another function 
and access variables from the outer function. (Often called Enclosing Scope)"""
def outer_func():
    x = 10
    def inner_func():
        nonlocal x
        x = 12
        
    inner_func()
    return x

print('5:','x =', outer_func())

""" 6. Create a program that defines a variable with the same name as a 
global variable inside a function and observe its scope."""
fruit = 'Apple'
def name_the_fruit():
    fruit = 'Banana'
    return fruit

new_fruit = name_the_fruit()

print('6:', 'Global fruit:', fruit)
print('  ', 'Local fruit:', new_fruit)
fruit = name_the_fruit()
print('  ', 'Global fruit:', fruit)