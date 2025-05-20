from herbivore import Herbivore

class Giraffe(Herbivore):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.type = 'giraffe'
    pass