# Class Method

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print (name, "is in", random.choice(cls.houses))


Hat.sort("Harry")  # since it's class method, "H"at is called

# or original way
#use classmethod when the sort is only use once

class Hat1:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat1()  # need to initialize
hat.sort("Bubu")

