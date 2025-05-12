
print('Lab 3 Functions')

"""1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere. Example: arrayCheck([1, 1, 2, 3, 1]) → True arrayCheck([1, 1, 2, 4, 1]) → False arrayCheck([1, 1, 2, 1, 2, 3]) → True"""

def arrayCheck(list):
    for i in range(len(list)):
        if list[i] == 1 and i+2 < len(list):
            if list[i+1] == 2:
                if list[i+2] == 3:
                    return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

"""
2. Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
Example:
stringBits('Hello') → 'Hlo' stringBits('Hi') → 'H' stringBits('Heeololeo') → 'Hello'
"""
def stringBits(string):
    new_string = ''
    for index in range(len(string)):
        if index %2 == 0:
            new_string += string[index]
    return new_string

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))
 
"""
3. Given a string, return a string where for every char in the original, # there are two chars.
doubleChar('The') → 'TThhee' doubleChar('AAbb') → 'AAAAbbbb' doubleChar('Hi-There') → 'HHii--TThheerree'
"""
def doubleChar(string):
    new_string = ''
    for char in string:
        new_string += char *2
    return new_string
    
print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))

"""
4. Return the number of even integers in the given array/list. Examples:
count_evens([2, 1, 2, 3, 4]) → 3 count_evens([2, 2, 0]) → 3 count_evens([1, 3, 5]) → 0
"""
def count_evens(array):
    count=0
    for int in array:
        if int % 2 == 0:
            count +=1
    return count

print(count_evens([2, 1, 2, 3, 4]) )
print(count_evens([2, 2, 0]) )
print(count_evens([1, 3, 5]) )

"""
5. Optional Lab:
You can actually make a simple command line game. You could put together everything
you've learned so far about Python. The game goes like this:
1. The computer will think of 3 digit number that has no repeating digits. 2. You will then guess a 3 digit number
3. The computer will then give back clues, the possible clues are:
Close: You've guessed a correct number but in the wrong position Match: You've guessed a correct number in the correct position Nope: You haven't guess any of the numbers correctly
4. Based on these clues you will guess again until you break the code with a perfect match!
There are a few things you will have to discover for yourself for this game! Here are some useful hints:
Try to figure out what this code is doing and how it might be useful to you import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
Another hint:
guess = input("What is your guess? ") print(guess)
Think about how you will compare the input to the random number, what format should they be in? Maybe some sort of sequence?
"""
import random

def createRandom():
    digits = [1,2,3,4,5,6,7,8,9]
    numbers = []
    for _ in range(3):
        rand = random.choice(digits)
        digits.remove(rand)
        numbers.append(rand)
    number_string = ''.join(map(str, numbers))
    return number_string

def generate_clues(user, computer):
    clues = []
    for i, x in enumerate(user):
        if x in computer:
            if computer[i] == x:
                clues.append("Match: You've guessed a correct number in the correct position")
            else:
                clues.append("Close: You've guessed a correct number but in the wrong position")
        else:
            clues.append("Nope: You haven't guess any of the numbers correctly")
    return clues

def checkresult(user, computer):
    return user == computer

def playGame():
    user_win = False
    computers_number = createRandom()

    while not user_win:
        user_guess = input('Guess a 3 digit number (no repeats): ')
        
        if checkresult(user_guess, computers_number):
            user_win = True
            print(f"YOU WON THE GAME!!! The computers number was {computers_number}")
        else: 
            clues = generate_clues(user_guess, computers_number)
            for i, clue in enumerate(clues, start=1):
                print(f'Clue for digit {i}: {clue}')
        
playGame()