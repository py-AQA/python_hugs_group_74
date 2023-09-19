# https://www.codewars.com/kata/632408defa1507004aa4f2b5
from helper import test


class Class:
    count = 1

    @staticmethod
    def get_number():
        prev = Class.count
        Class.count <<= 1
        return prev


# проверка
test.assert_equals(Class.get_number(), 1, "1st call should return 1")
test.assert_equals(Class.get_number(), 2, "2nd call should return 2")
test.assert_equals(Class.get_number(), 4, "3rd call should return 4")
test.assert_equals(Class.get_number(), 8, "4th call should return 8")
test.assert_equals(Class.get_number(), 16, "5th call should return 16")
