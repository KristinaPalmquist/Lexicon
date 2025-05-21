from animal import Animal

class Herbivore(Animal):
    type = 'herbivore'
    food_energy_increase = 10
    sleep_energy_increase = 20
    sound_energy_decrease = 10
    food = 'veggies'
   
    def __init__(self, age, name):
        super().__init__(age, name)
        
    def eat(self):
        if self.energy_level + self.food_energy_increase <= 100:
            self.change_energy_level(self.food_energy_increase)
            print(f'{self.name} the {self.type} has eaten {self.food}.. Energy level is now {self.energy_level}')
        else:
            print(f'{self.name} is not hungry')
            
    def sleep(self):
        if self.energy_level + self.sleep_energy_increase <= 100:
            self.change_energy_level(self.sleep_energy_increase)
            print(f'{self.name} slept for a while')
        else:
            print(f'{self.name} is not tired')      
            
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'{self.name} the {self.type}\n\nMooo\n')