from animal import Animal

class Carnivore(Animal):
    type = 'carnivore'
    food_energy_increase = 20
    sleep_energy_increase = 10
    food = 'meat'
    
    def __init__(self, age, name):
        super().__init__(age, name)
        
    def eat(self):
        if self.energy_level + self.food_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.food_energy_increase)
            print(f'\n{self.name} the {self.type} has eaten {self.food}.\nEnergy level is now {self.energy_level}')
        else:
            print(f'\n{self.name} is not hungry')
            
    def sleep(self):
        if self.energy_level + self.sleep_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.sleep_energy_increase)
            print(f'\n{self.name} slept for a while')
        else:
            print(f'\n{self.name} is not tired')   
               
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'\n{self.name} the {self.type}:\n\nRooaar!\n')