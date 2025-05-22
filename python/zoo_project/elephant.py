from herbivore import Herbivore

class Elephant(Herbivore):
    type = 'elephant'
    food = 'tree bark'
    
    def __init__(self, age, name):
        super().__init__(age, name)
    
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'\n{self.name} the {self.type}:\n\nTrumpet!\n')