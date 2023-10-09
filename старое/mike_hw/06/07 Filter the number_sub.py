# https://www.codewars.com/kata/55b051fac50a3292a9000025
import re
from helper import test


def filter_string(string):
    return int(''.join(re.sub("[^0-9]", '', string)))
    # return int(''.join(re.sub("\D", '', string)))


# проверка
test.assert_equals(filter_string("123"), 123, 'Just return the numbers')
test.assert_equals(filter_string("a1b2c3"), 123, 'Just return the numbers')
test.assert_equals(filter_string("aa1bb2cc3dd"), 123, 'Just return the numbers')
test.assert_equals(filter_string("aa 112 3dd"), 1123, 'Just return the numbers')
test.assert_equals(filter_string("11bb2c23c3"), 112233, 'Just return the numbers')
