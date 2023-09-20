# https://www.codewars.com/kata/55c1d030da313ed05100005d
from helper import test
from math import pi


class Sphere(object):
    def __init__(self, r, m):
        self.r = r
        self.m = m

    def get_radius(self):
        return self.r

    def get_mass(self):
        return self.m

    def get_volume(self):
        return round((4 / 3) * pi * self.r ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.r ** 2, 5)

    def get_density(self):
        return round(self.m / ((4 / 3) * pi * self.r ** 3), 5)


# проверка
ball = Sphere(2, 50)
test.assert_equals(ball.get_radius(), 2, "Check radius")
test.assert_equals(ball.get_mass(), 50, "Check mass")
test.assert_equals(ball.get_volume(), 33.51032, "Check volume")
test.assert_equals(ball.get_surface_area(), 50.26548, "Check area")
test.assert_equals(ball.get_density(), 1.49208, "Check density")
