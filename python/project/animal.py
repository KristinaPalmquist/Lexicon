class Animal:
    instances = []
    energy_level = 100
    max_energy_level = 100
    food_energy_increase = 10
    sleep_energy_increase = 10
    sound_energy_decrease = 10
    play_energy_decrease = 20
    index_number = 1
    
    @classmethod
    def change_energy_level(cls, change):
        cls.energy_level += change
        if cls.energy_level < cls.max_energy_level/2:
            print(f'Energy level is too low! {cls.name} needs to eat or sleep ASAP')
            
    @classmethod
    def list_instances(cls):
        print('Animals in the zoo:')        
        print('-'*50)
        print('NR:'.ljust(10), 'NAME:'.ljust(20), 'TYPE:'.ljust(10), 'AGE:'.rjust(5))
        for inst in cls.instances:
            print(str(inst.index).ljust(10), inst.name.ljust(20), inst.type.capitalize().ljust(10), str(inst.age).rjust(4))
        print('-'*50)
    
    def __init__(self, name, age):
        Animal.instances.append(self)
        self.name = name
        self.age = age
        self.type = 'animal'
        self.index = Animal.index_number
        Animal.index_number += 1
    def eat(self):
        if self.energy_level + self.food_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.food_energy_increase)
            print(f'{self.name} has eaten. Energy level is now {self.energy_level}')
        else:
            print(f'{self.name} is not hungry')
    def sleep(self):
        if self.energy_level + self.sleep_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.sleep_energy_increase)
            print(f'{self.name} slept for a while')
        else:
            print(f'{self.name} is not tired')      
    def make_sound(self):
        if self.energy_level > self.sound_energy_decrease:
            self.change_energy_level(self.sound_energy_decrease)
            print(f'{self.name} made a sound')
        else:
            print(f'{self.name} did not have enough energy to make a sound. Energy level is only {self.energy_level}')
    def play(self):
        if self.energy_level > self.play_energy_decrease:
            self.change_energy_level(self.play_energy_decrease)
            print(f'{self.name} played with their friends')
        else:
            print(f'{self.name} did not have enough energy to play. Energy level is only {self.energy_level}')