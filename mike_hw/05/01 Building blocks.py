# https://www.codewars.com/kata/55b75fcf67e558d3750000a3
from helper import test


class Block:
    def __init__(self, lst):
        self.width, self.length, self.height = lst

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.height * self.length + self.height * self.width + self.width * self.length)


# проверка
block1 = Block([2, 2, 2])
test.assert_equals(block1.get_width(), 2)
test.assert_equals(block1.get_length(), 2)
test.assert_equals(block1.get_height(), 2)
test.assert_equals(block1.get_volume(), 8)
test.assert_equals(block1.get_surface_area(), 24)
