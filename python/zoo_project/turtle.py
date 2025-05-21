from herbivore import Herbivore

class Turtle(Herbivore):
    type = 'turtle'
    food = 'grass'
    
    def __init__(self, age, name):
        super().__init__(age, name)
        
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'{self.name} the {self.type}:\n\nPurr, croak, sigh.\n')