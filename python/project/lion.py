from carnivore import Carnivore

class Lion(Carnivore):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.type = 'lion'
    