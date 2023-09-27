# https://www.codewars.com/kata/557d9e4d155e2dbf050000aa
import re
import math
from helper import test


def anything(thing):
    class Anything:
        __ne__ = __lt__ = __gt__ = __le__ = __ge__ = __eq__ = lambda *args: True

    """
        try to return anything else :)
    """
    return Anything()


# проверка
test.expect(anything({}) != [], "A Dictionary can not equal to a List")
test.expect(anything('Hello') < 'World', "The String Hello can be less than the String world")
test.expect(anything(80) > 81, "80 can be greater than 81")
test.expect(anything(re) >= re, "A module re can be greater than re")
test.expect(anything(re) <= math, "A module re can be less than or equal to the module math")
test.expect(anything(5) == ord, "A number such as 5 can be equal to an undefined variable ord")


