from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = None, age = 0.0):
        super().__init__(id, condition, age)
        self.fabric = fabric

#inherit get_category from Item

    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."