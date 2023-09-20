# https://www.codewars.com/kata/55ddcef532f8678af1000006
from helper import test


class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if new_name[0].isupper() and new_name.isalnum():
            cls.__name__ = new_name
        else:
            raise ValueError('ups!')

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"


# проверка
class MyClass(ReNameAbleClass):
    pass


myObject = MyClass()
test.assert_equals(str(myObject), "Class name is: MyClass", "Original class name shouldn't be changed yet...")

myObject.change_class_name("UsefulClass")
test.assert_equals(str(myObject), "Class name is: UsefulClass", "New class name should be as boss wanted to!")

myObject.change_class_name("SecondUsefulClass")
test.assert_equals(str(myObject), "Class name is: SecondUsefulClass", "New class name should be as boss wanted to!")