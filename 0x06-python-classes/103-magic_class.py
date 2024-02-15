import math


class MagicClass:
    def__init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
