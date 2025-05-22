class Animal:
    type = 'animal'
    instances = []
    energy_level = 75
    max_energy_level = 100
    food_energy_increase = 10
    sleep_energy_increase = 10
    sound_energy_decrease = -10
    play_energy_decrease = -20
    food = 'food'
    _id_counter = 1
    
    @classmethod
    def change_energy_level(cls, change):
        cls.energy_level += change
        if cls.energy_level < cls.max_energy_level/2:
            print(f'\nEnergy level is too low!\n{cls.name} needs to eat or sleep ASAP!')
            
    @classmethod
    def list_instances(cls):
        print('\nAnimals in the zoo:')        
        print('-'*50)
        print('NR:'.ljust(5), 'NAME:'.ljust(20), 'TYPE:'.ljust(10), 'AGE:'.rjust(4), 'ENERGY:'.rjust(5))
        for inst in cls.instances:
            print(str(inst.index).ljust(5), inst.name.ljust(20), inst.type.capitalize().ljust(10), str(inst.age).rjust(4), str(inst.energy_level).rjust(5))
        print('-'*50)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.index = Animal._id_counter
        Animal._id_counter += 1
        Animal.instances.append(self)
        
    def eat(self):
        if self.energy_level + self.food_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.food_energy_increase)
            print(f'\n{self.name} has eaten {self.food}.\nEnergy level is now {self.energy_level}.')
        else:
            print(f'\n{self.name} is not hungry')
            
    def sleep(self):
        if self.energy_level + self.sleep_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.sleep_energy_increase)
            print(f'\n{self.name} slept for a while.\nEnergy level is now {self.energy_level}.')
        else:
            print(f'\n{self.name} is not tired.')      
            
    def make_sound(self):
        if self.energy_level > self.sound_energy_decrease:
            self.change_energy_level(self.sound_energy_decrease)
            print(f'\n{self.name} the {self.type} made a sound.')
        else:
            print(f'\n{self.name} did not have enough energy to make a sound.\nEnergy level is only {self.energy_level}.')
            
    def play(self):
        if self.energy_level > self.play_energy_decrease:
            self.change_energy_level(self.play_energy_decrease)
            print(f'\n{self.name} the {self.type} played with their friends.\nEnergy level is now {self.energy_level}.')
        else:
            print(f'\n{self.name} did not have enough energy to play.\nEnergy level is only {self.energy_level}.')