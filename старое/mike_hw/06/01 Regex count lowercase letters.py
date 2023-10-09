# https://www.codewars.com/kata/56a946cd7bd95ccab2000055
import re
from helper import test


def lowercase_count(strng):
    return len(re.findall("[a-z]", strng))


# проверка
test.assert_equals(lowercase_count("abc"), 3)
test.assert_equals(lowercase_count("abcABC123"), 3)
test.assert_equals(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
test.assert_equals(lowercase_count(""), 0)
test.assert_equals(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
test.assert_equals(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)
