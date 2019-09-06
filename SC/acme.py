from random import randint


class Product:
    '''Creating product class with generic fields
    '''
    def __init__(self, name: str, price: int=10, weight: int=20, 
                 flammability: float=0.5,
                 identifier: int=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        stealability = self.price/self.weight
        if stealability < .5:
            return "Not so stealable..."
        elif stealability < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explodibility = self.flammability*self.weight
        if explodibility < 10:
            return "...fizzle."
        elif explodibility < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name: str, price: int=10, weight: int=10, 
                 flammability: float=0.5,
                 identifier: int=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles"
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
