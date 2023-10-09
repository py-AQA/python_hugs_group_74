# https://www.codewars.com/kata/563f879ecbb8fcab31000041
from helper import test


def factory(x):
    def inner(lst):
        return [x * y for y in lst]

    return inner


# проверка
my_arr = [1, 2, 3]

threes = factory(3)
test.assert_equals(threes(my_arr), [3, 6, 9])

fives = factory(5)
test.assert_equals(fives(my_arr), [5, 10, 15])
