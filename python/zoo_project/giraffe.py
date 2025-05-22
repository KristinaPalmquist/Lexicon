from herbivore import Herbivore

class Giraffe(Herbivore):
    type = 'giraffe'
    food = 'leaves'
    
    def __init__(self, age, name):
        super().__init__(age, name)
    
    def make_sound(self):
        self.change_energy_level(self.sound_energy_decrease)
        print(f'\n{self.name} the {self.type}:\n\nGrunt, snort!\n')