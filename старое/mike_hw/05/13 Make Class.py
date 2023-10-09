# https://www.codewars.com/kata/5d774cfde98179002a7cb3c8
from helper import test


def make_class(*names):
    class _:
        def __init__(self, *values):
            [setattr(self, n, v) for n, v in zip(names, values)]

    return _


# проверка
class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color


Animel = make_class("name", "species", "age", "health", "weight", "color")

dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

test.assert_equals(dog1.name, dog2.name)
test.assert_equals(dog1.species, dog2.species)
test.assert_equals(dog1.age, dog2.age)
test.assert_equals(dog1.health, dog2.health)
test.assert_equals(dog1.weight, dog2.weight)
test.assert_equals(dog1.color, dog2.color)
