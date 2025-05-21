from animal import Animal
from giraffe import Giraffe
from turtle import Turtle
from elephant import Elephant
from lion import Lion
from fox import Fox
from bear import Bear
from visitor import Visitor

def main():
    print('-'*50)
    print("Welcome to Lexicon Zoo!!!")
    print('-'*50)
    register_visitors()
    menu()
    
    
def register_visitors():
    while True:
        try:
            number_of_visitors = int(input('How many visitors are there in your group (including yourself)?\n'))
            if 0 <= number_of_visitors <= 10:
                break
            else:
                print('Invalid input. Maximum number of visitors is 10')
        except ValueError:
            print('Invalid input. Please enter number of visitors')
    for index in range(number_of_visitors):    
        name = input(f'Enter the name of visitor number {index+1}:\n')
        while True:
            try:
                age = int(input(f'Enter the age of visitor number {index+1}:\n'))
                if 0 <= age <= 130:
                    break
                else:
                    print('Invalid input. Enter a valid age in the range 0-130')
            except ValueError:
                print('Invalid input. Please enter number as age')
        Visitor(name, age)
    Visitor.list_instances()
    
def create_new_animal(animal_class):
    animal_name = input(f"What's the {animal_class.type}s name?\n").capitalize()
    while True:
            try:
                animal_age = int(input(f"How old is the {animal_class.type}?\n"))
                if 0 <= animal_age <= 1000:
                    break
                else:
                    print('Invalid input. Enter a valid age in the range 0-1000')
            except ValueError:
                print('Invalid input. Please enter number as age')
    animal = animal_class(animal_name, animal_age)
    return animal
        
def new_animal():
    user_animal_choice = input(f"""
    What type of animal should be added?
    {'-'*46}
    Enter B for BEAR
    Enter E for ELEPHANT
    Enter F for FOX
    Enter G for GIRAFFE
    Enter L for LION
    Enter T for TURTLE
    """)
  
    animal = ()
    match user_animal_choice[0].upper():
        case 'G' | 'giraffe':
            animal = create_new_animal(Giraffe)
        case 'L' | 'lion':
            animal = create_new_animal(Lion)
        case 'T' | 'turtle':
            animal = create_new_animal(Turtle)
        case 'B' | 'bear':
            animal = create_new_animal(Bear)
        case 'E' | 'elephant':
            animal = create_new_animal(Elephant)
        case 'F' | 'fox':
            animal = create_new_animal(Fox)
        case _:
            print("I don't understand.\n Please choose one of the listed animals.")
            new_animal()

    print(f'\nYour new animal {animal.name} has been added to the zoo!\n')
    Animal.list_instances()
    
def menu():
    user_menu_choice = input(f"""
    What do you want to do?
    {'-'*46}
    Enter 1 to Add an animal
    Enter 2 to Feed an animal
    Enter 3 to let an animal Sleep
    Enter 4 to hear an animals Make sound
    Enter 5 to let an animal Play
    Enter 6 to List all Animals
    Enter 7 to List all Visitors
    Enter 8 to Exit the zoo
    """).lower()

    match user_menu_choice:
        case '1' | 'a':
            new_animal()
        case '2' | 'f':
            Animal.list_instances()
            user_animal_choice = input('Enter the number of the animal you want to feed:\n')
            user_animal  = next((instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
            user_animal.eat()
        case '3' | 's':
            Animal.list_instances()
            user_animal_choice = input('Enter the number of the animal that needs to sleep:\n')
            user_animal  = next((instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
            user_animal.sleep()
        case '4' | 'm':
            Animal.list_instances()
            user_animal_choice = input('Enter the number of the animal whos sound you want to hear:\n')
            user_animal  = next((instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
            user_animal.make_sound()
        case '5' | 'p':
            Animal.list_instances()
            user_animal_choice = input("Enter the number of the animal that wants to play:\n")
            user_animal  = next((instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
            user_animal.play()
        case '6' | 'la':
            Animal.list_instances()   
        case '7' | 'lv':
            Visitor.list_instances()        
        case '8' | 'esc' | 'exit' | 'e' | 'quit' | 'q':
            exit()
        case _:
            print("I don't understand. Please choose something from the menu")
    menu()



Visitor('Simon', 78)
Visitor('Agda', 56)
Visitor('Benny', 4)

Giraffe('Simon', 2)
Lion('Fester', 7)
Fox('Anabel', 2)
Bear('Bob', 10)
Turtle('Tutu', 89)
Elephant('Ikaros', 24)



main()