from animal import Animal
from giraffe import Giraffe
from lion import Lion
from visitor import Visitor

def main():
    print("Welcome to Lexicon Zoo!!!")
    register_visitors()
    menu()
    
    
def register_visitors():
    number_of_visitors= input('How many visitors are there in your group (including yourself)?\n')
    for index in range(int(number_of_visitors)):
        name = input(f'Enter the name of visitor number {index+1}:\n')
        age = input(f'Enter the age of visitor number {index+1}:\n')
        new_visitor = Visitor(name, age)
    print(Visitor.list_instances())
        
def new_animal():
    user_animal_choice = input("""
                       What type of animal should be added?
                       Enter G for GIRAFFE
                       Enter L for LION
                       """)
    animal_name = input("""What should it be called?""")
    
    if user_animal_choice[0].upper() == 'G':
        new_animal = Giraffe(animal_name)
          
    elif user_animal_choice[0].upper() == 'L':
        new_animal = Lion(animal_name)
    
def menu():
    user_menu_choice = input("""
                       What do you want to do?
                       Enter 1 to Add an animal
                       Enter 2 to Feed an animal
                       Enter 3 to let an animal Sleep
                       Enter 4 to hear an animals Make sound
                       Enter 5 to let an animal Play
                       Enter 6 to List all Animals
                       Enter 7 to List all Visitors
                       Enter 8 to Exit the zoo
                       """).lower()
    
    # if user_menu_choice == '1':
    #     new_animal()
    # elif user_menu_choice == '2':
    #     Animal.list_instances()
    #     user_animal_choice = input("""
    #                    Enter the number of the animal you want to feed
    #                    """)
    #     user_animal_choice = 
        
    #     user_animal_choice.eat()
    # elif user_menu_choice == '3':
    #     Animal.list_instances()
    #     user_animal_choice = input("""
    #                    Enter the number of the animal that needs to sleep
    #                    """)
    #     user_animal_choice.sleep()
    # elif user_menu_choice == '4':
    #     Animal.list_instances()
    #     user_animal_choice = input("""
    #                    Enter the number of the animal whos sound you want to hear
    #                    """)
    #     user_animal_choice.make_sound()
    # elif user_menu_choice == '5':
    #     Animal.list_instances()
    #     user_animal_choice = input("""
    #                    Enter the number of the animal that wants to play
    #                    """)
    #     user_animal_choice.play()
    # elif user_menu_choice == '6':
    #     Animal.list_instances()   
    # elif user_menu_choice == '7':
    #     Visitor.list_instances()        
    # elif user_menu_choice in ('8', 'esc', 'exit', 'quit', 'q'):
    #     exit()
    # else:
    #     print("I don't understand. Please choose something from the menu")
    # menu()
    match user_menu_choice:
        case '1':
            new_animal()
        case '2':
            Animal.list_instances()
            user_animal_choice = input("""
                        Enter the number of the animal you want to feed
                        """)
            # user_animal_choice = 
            
            user_animal_choice.eat()
        case '3':
            Animal.list_instances()
            user_animal_choice = input("""
                        Enter the number of the animal that needs to sleep
                        """)
            user_animal_choice.sleep()
        case '4':
            Animal.list_instances()
            user_animal_choice = input("""
                        Enter the number of the animal whos sound you want to hear
                        """)
            user_animal_choice.make_sound()
        case '5':
            Animal.list_instances()
            user_animal_choice = input("""
                        Enter the number of the animal that wants to play
                        """)
            user_animal_choice.play()
        case '6':
            Animal.list_instances()   
        case '7':
            Visitor.list_instances()        
        case '8' | 'esc' | 'exit' | 'quit' | 'q':
            exit()
        case _:
            print("I don't understand. Please choose something from the menu")
    menu()

vis1 = Visitor('Simon', 78)
vis2 = Visitor('Agda', 56)
vis3 = Visitor('Benny', 4)
# Visitor.list_instances()

a1 = Giraffe('Simon', 2)
a2 = Lion('Fester', 7)
# Animal.list_instances()



main()
# menu()