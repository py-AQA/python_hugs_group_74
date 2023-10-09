# https://www.codewars.com/kata/5882b052bdeafec15e0000e6
from helper import test


class Quark(object):
    def __init__(self, color, flavor):
        self.baryon_number = 1.0 / 3
        self.color = color
        self.flavor = flavor

    def interact(self, quark):
        quark.color, self.color = self.color, quark.color


# проверка
q1 = Quark("red", "up")
q2 = Quark("blue", "strange")

test.assert_equals(q1.color, "red")
test.assert_equals(q2.flavor, "strange")
test.assert_equals(q2.baryon_number, 1.0 / 3)
q1.interact(q2)
test.assert_equals(q1.color, "blue")
test.assert_equals(q2.color, "red")
