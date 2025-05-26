from animal import Animal
from giraffe import Giraffe
from turtle import Turtle
from elephant import Elephant
from lion import Lion
from fox import Fox
from bear import Bear
from visitor import Visitor

show_full_menu = True
show_animal_menu = True


def main():
    print('')
    print('-'*50)
    print("Welcome to Lexicon Zoo!!!")
    print('-'*50)
    register_visitors()
    menu()


def register_visitors():
    while True:
        try:
            number_of_visitors = int(
                input(
                    'How many visitors are there in your group '
                    '(including yourself)?\n'
                )
            )
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
                age = int(
                    input(f'Enter the age of visitor number {index+1}:\n')
                )
                if 0 <= age <= 130:
                    break
                else:
                    print(
                        'Invalid input. Enter a valid age in the range 0-130'
                    )
            except ValueError:
                print('Invalid input. Please enter number as age')
        Visitor(name, age)
    Visitor.list_instances()


def create_new_animal(animal_class):
    animal_name = input(
        f"What's the {animal_class.type}s name?\n"
    ).capitalize()
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
    global show_animal_menu
    animal = None
    while animal is None:
        if show_animal_menu:
            user_animal_choice = input(f"""
    What type of animal do you want to add?
    {'-'*46}
    Enter B for BEAR
    Enter E for ELEPHANT
    Enter F for FOX
    Enter G for GIRAFFE
    Enter L for LION
    Enter T for TURTLE
    """).lower()
            show_animal_menu = False
        else:
            user_animal_choice = input(
                "\nWhat type of animal do you want to add?\n"
                "Type 'menu' to see the options:\n"
            ).lower()
            if user_animal_choice == 'menu':
                show_animal_menu = True
                continue

        match user_animal_choice[0]:
            case 'g' | 'giraffe':
                animal = create_new_animal(Giraffe)
            case 'l' | 'lion':
                animal = create_new_animal(Lion)
            case 't' | 'turtle':
                animal = create_new_animal(Turtle)
            case 'b' | 'bear':
                animal = create_new_animal(Bear)
            case 'e' | 'elephant':
                animal = create_new_animal(Elephant)
            case 'f' | 'fox':
                animal = create_new_animal(Fox)
            case _:
                print("I don't understand.")
                print("Please choose one of the listed animals.")
                continue

    print(f'\nYour new animal {animal.name} has been added to the zoo!\n')
    Animal.list_instances()


def menu():
    global show_full_menu
    while True:
        if show_full_menu:
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
            show_full_menu = False
        else:
            user_menu_choice = input(
                "\nWhat do you want to do?\n"
                "Type 'menu' to see the options:\n"
            ).lower()
            if user_menu_choice == 'menu':
                show_full_menu = True
                continue

        match user_menu_choice:
            case '1' | 'a':
                new_animal()
            case '2' | 'f':
                Animal.list_instances()
                while True:
                    user_animal_choice = input(
                        'Enter the number of the animal you want to feed:\n'
                    )
                    if not user_animal_choice.isdigit():
                        print("Invalid input. Please enter a valid number.")
                        continue
                    user_animal  = next(
                        (instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
                    if user_animal is None:
                        print(
                            "No animal found with that number. "
                            "Please enter a valid number."
                        )
                        continue
                    user_animal.eat()
                    break
            case '3' | 's':
                Animal.list_instances()
                while True:
                    user_animal_choice = input(
                        'Enter the number of the animal that needs to sleep:\n'
                    )
                    if not user_animal_choice.isdigit():
                        print("Invalid input. Please enter a valid number.")
                        continue
                    user_animal  = next(
                        (instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
                    if user_animal is None:
                        print(
                            "No animal found with that number. "
                            "Please enter a valid number."
                        )
                        continue
                    user_animal.sleep()
                    break
            case '4' | 'm':
                Animal.list_instances()
                while True:
                    user_animal_choice = input(
                        'Enter the number of the animal whose sound you want '
                        'to hear:\n'
                    )
                    if not user_animal_choice.isdigit():
                        print("Invalid input. Please enter a valid number.")
                        continue
                    user_animal  = next(
                        (instan for instan in Animal.instances 
                            if user_animal_choice == str(instan.index)), None)
                    if user_animal is None:
                        print(
                            "No animal found with that number. "
                            "Please enter a valid number."
                        )
                        continue
                    user_animal.make_sound()
                    break
            case '5' | 'p':
                Animal.list_instances()
                while True:
                    user_animal_choice = input(
                        "Enter the number of the animal that wants to play:\n"
                    )
                    if not user_animal_choice.isdigit():
                        print("Invalid input. Please enter a valid number.")
                        continue
                    user_animal  = next(
                        (instan for instan in Animal.instances
                            if user_animal_choice == str(instan.index)), None)
                    if user_animal is None:
                        print(
                            "No animal found with that number. "
                            "Please enter a valid number."
                        )
                        continue
                    user_animal.play()
                    break
            case '6' | 'la':
                Animal.list_instances()   
            case '7' | 'lv':
                Visitor.list_instances()        
            case '8' | 'esc' | 'exit' | 'e' | 'quit' | 'q':
                print('')
                print('-'*50)
                print("Thank's for your visit!\n"
                      "Hope you had a wonderful day!!!")
                print('-'*50)
                exit()
            case _:
                print(
                    "I don't understand. Please choose something from the menu"
                )
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
