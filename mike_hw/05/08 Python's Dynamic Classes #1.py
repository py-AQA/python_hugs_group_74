# https://www.codewars.com/kata/pythons-dynamic-classes-number-1
from helper import test


def class_name_changer(cls, new_name):
    if new_name and new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError('ups!')


# проверка
class MyClass:
    pass


test.assert_equals(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass")
test.assert_equals(MyClass.__name__, "UsefulClass")
