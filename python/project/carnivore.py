from animal import Animal

class Carnivore(Animal):
    food_energy_increase = 20
    sleep_energy_increase = 10
   
    def __init__(self, age, name):
        super().__init__(age, name)
        self.type = 'carnivore'
    def eat(self):
        if self.energy_level + self.food_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.food_energy_increase)
            print(f'{self.name} has had a meaty meal. Energy level is now {self.energy_level}')
        else:
            print(f'{self.name} is not hungry')
    def sleep(self):
        if self.energy_level + self.sleep_energy_increase <= self.max_energy_level:
            self.change_energy_level(self.sleep_energy_increase)
            print(f'{self.name} slept for a while')
        else:
            print(f'{self.name} is not tired')      
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'Rooaar!')