from uuid import uuid4

class Item:
    def __init__(self, id=None, condition = 0.0, age = 0.0):
        self.id = uuid4().int if id == None else id
        self.condition = condition if condition else 0.0
        self.age = age if age else 0.0

    def get_category(self):
        #return the string holding the name of the class
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition in range(1,2):
            return "bad condition"
        elif self.condition in range(2,4):
            return "okay condition"
        elif self.condition in range(4,6):
            return "great condition"
