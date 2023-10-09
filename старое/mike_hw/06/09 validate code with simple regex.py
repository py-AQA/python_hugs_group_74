# https://www.codewars.com/kata/56a25ba95df27b7743000016
import re
from helper import test


def validate_code(code):
    return bool(re.match("^[1-3]", str(code)))


# проверка
test.assert_equals(validate_code(123), True)
test.assert_equals(validate_code(248), True)
test.assert_equals(validate_code(8), False)
test.assert_equals(validate_code(321), True)
test.assert_equals(validate_code(9453), False)
