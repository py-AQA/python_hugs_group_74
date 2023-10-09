# https://www.codewars.com/kata/64c766dd16982000173d5ba1
from helper import test


class Menu:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.indx = 0

    def to_the_right(self):
        self.indx += 1
        self.indx %= len(self.lst)

    def to_the_left(self):
        if not self.indx:
            self.indx = len(self.lst)
        self.indx -= 1

    def display(self):
        return f"{list(list(x) if i == self.indx else x for i, x in enumerate(self.lst))}"


# проверка
menu = Menu(['1', '2', '3'])
menu2 = Menu(["a", "b", "c"])

test.assert_equals(menu.display(), "[['1'], '2', '3']")

menu.to_the_right()
test.assert_equals(menu.display(), "['1', ['2'], '3']")

menu.to_the_right()
test.assert_equals(menu.display(), "['1', '2', ['3']]")

menu.to_the_right()
test.assert_equals(menu.display(), "[['1'], '2', '3']")

test.assert_equals(menu2.display(), "[['a'], 'b', 'c']")

menu2.to_the_left()
test.assert_equals(menu2.display(), "['a', 'b', ['c']]")

menu2.to_the_left()
test.assert_equals(menu2.display(), "['a', ['b'], 'c']")

menu2.to_the_left()
test.assert_equals(menu2.display(), "[['a'], 'b', 'c']")