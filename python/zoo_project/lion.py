from carnivore import Carnivore

class Lion(Carnivore):
    type = 'lion'
    food = 'zebra'
    
    def __init__(self, age, name):
        super().__init__(age, name)
        
    