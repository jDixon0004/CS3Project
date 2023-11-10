from random import randint

class Package:
    def __init__(self, id_number:int = None, dimensions:tuple = None, weight:float = None):
        self.__id_number = id_number
        self.__dimensions = dimensions
        self.__weight = weight

        if self.id_number is None:
            self.__generate_id_number()
    
    def __generate_id_number(self):
        '''
        Generate a random id number that is not already taken by another package
        '''
        id_number = randint(0, 99999999)
        while id_number in package_db: # come back and add package_db later
            id_number = randint(0, 99999999)
        
        self.__id_number = id_number
    
    def get_weight(self):
        return self.__weight
    
    def get_id(self):
        return self.__id_number
    
    def __eq__(self, o):
        if isinstance(o, int):
            return self.__id_number == o
        
        elif isinstance(o, Package):
            return self.__id_number == o.__id_number
        
        return False