#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?

In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.

The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.

*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the factory we chose (Dog or Cat, or random_animal)
This works because both Dog/Cat and random_animal respect a common
interface (callable for creation and .speak()).
Now my application can create pets abstractly and decide later,
based on my own criteria, dogs over cats.

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR80
Provides a way to encapsulate a group of individual factories.
"""

class MazeFactory(object):
    """docstring for MazeFactory"""
    def __init__(self, arg):
        super(MazeFactory, self).__init__()
        self.arg = arg
    def makeWall(self,):
        pass
    def makeRoom(self,):
        pass
    def makeDoor(self,):


class BombMazeFactory(MazeFactory):
    """docstring for BombMazeFactory"""
    def __init__(self, arg):
        super(BombMazeFactory, self).__init__()
        self.arg = arg
    def makeRoom():
        return BombRoom()
        
class EnhancedMazeFactory(MazeFactory):
    """docstring for EnhancedMazeFactory"""
    def __init__(self, arg):
        super(EnhancedMazeFactory, self).__init__()
        self.arg = arg
    def makeDoor(self):
        return EnhancedFancyDoor

class Wall:
    pass
class Room:
    pass
class Door:
    pass

class BombRoom(Room):
    pass
class EnhancedFancyDoor(Door):
    pass

'''
Or parameterized Factory type + store classes inside
'''

class Singleton(type):
    """docstring for Singleton"""
    _instances={}
    def __call__(cls, , *args, **kwargs):
        if not cls in _instances:
            _instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return _instances[cls]

        
class MazeFactory(object,metaclass=Singleton):
    """docstring for MazeFactory"""
    def __init__(self, type_):
        super(MazeFactory, self).__init__()
        self.tpye = type_
        self.dict = {
            'BombMazeFactory': {
                'wall': Wall,
                'room': BombRoom,
                'door': Door
            },
            'EnhancedMazeFactory': {
                'wall': Wall,
                'room': Room,
                'door': EnhancedFancyDoor            }
        }

    #support flexible new kinds of products.
    #eg makeDoor, makeWall, makeRoom. Even in the furture makeDesk
    #dont' have to add new functions to support
    def make(self, item):
        return self.dict[self.type][item]()

    def makeWall(self,):
        return self.dict[self.type]['wall']()
    def makeRoom(self,):
        pass
    def makeDoor(self,):

        

import random


class PetShop(object):

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Additional factories:

# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])()


# Show pets with various factories
if __name__ == "__main__":

    # A Shop that sells only cats
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # A shop that sells random animals
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

### OUTPUT ###
# We have a lovely Cat
# It says meow
#
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================
