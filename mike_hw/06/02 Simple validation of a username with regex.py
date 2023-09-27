# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023
import re
from helper import test


def validate_usr(username):
    return bool(re.fullmatch("[a-z0-9_]{4,16}", username))


# проверка
test.assert_equals(validate_usr('asddsa'), True)
test.assert_equals(validate_usr('a'), False)
test.assert_equals(validate_usr('Hass'), False)
test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
test.assert_equals(validate_usr(''), False)
test.assert_equals(validate_usr('____'), True)
test.assert_equals(validate_usr('012'), False)
test.assert_equals(validate_usr('p1pp1'), True)
test.assert_equals(validate_usr('asd43 34'), False)
test.assert_equals(validate_usr('asd43_34'), True)
