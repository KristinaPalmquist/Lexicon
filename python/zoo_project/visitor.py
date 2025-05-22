class Visitor:
    instances = []
    
    @classmethod
    def list_instances(cls):
        print('\nRegistered visitors:')
        print('-'*50)
        print('VISITOR NAME:'.ljust(20), 'AGE:'.rjust(5))
        for inst in cls.instances:
            print(inst.name.ljust(20), str(inst.age).rjust(4))
        
        print('-'*50)
            
    
    def __init__(self, name, age):
        Visitor.instances.append(self)
        self.name = name
        self.age = age
        
