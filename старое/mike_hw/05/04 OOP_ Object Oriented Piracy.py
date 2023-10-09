# https://www.codewars.com/kata/54fe05c4762e2e3047000add
from helper import test


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20


# проверка
EmptyShip = Ship(0, 0)
test.assert_equals(EmptyShip.is_worth_it(), False)
Boat = Ship(15, 20)
test.assert_equals(Boat.is_worth_it(), False)
biggerBoat = Ship(35, 20)
test.assert_equals(biggerBoat.is_worth_it(), False)
