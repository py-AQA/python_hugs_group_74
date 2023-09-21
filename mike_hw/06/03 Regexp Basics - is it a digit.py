# https://www.codewars.com/kata/567bf4f7ee34510f69000032
import re
from helper import test


def is_digit(n):
    return bool(re.fullmatch("\d", n))


# проверка
test.assert_equals(is_digit(""), False)
test.assert_equals(is_digit("7"), True)
test.assert_equals(is_digit(" "), False)
test.assert_equals(is_digit("a"), False)
test.assert_equals(is_digit("a5"), False)
