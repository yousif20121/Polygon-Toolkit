# Import necessary modules.
from math import *
from turtle import *


# Define a base class for polygons.
class Polygon:
    """
    Base class for polygons.
    """
    def __init__(self, number_of_sides=0, side_len=0):
        """
        Initialize a Polygon with a specified number of sides and side length.

        :param number_of_sides: Number of sides of the polygon.
        :param side_len: Length of each side.
        """
        self.__number_of_sides = number_of_sides
        self.__side_len = side_len

    def perimeter(self):
        """
         Calculate the perimeter of the polygon.

        :return: Perimeter of the polygon.
        """
        return self.__number_of_sides * self.__side_len

    def area(self):
        """
        Returns a message as the base class doesn't provide a specific area calculation.

        :return: A message indicating that more data is needed to calculate the area.
        """
        return f"Polygon area: I need more data to do that"

    def draw(self):
        """
        Draw the polygon using the Turtle graphics library.
        """
        for i in range(self.__number_of_sides):
            forward(self.__side_len + 100)
            left(360 / self.__number_of_sides)


# Define a subclass Pentagon that inherits from Polygon.
class Pentagon(Polygon):
    """
    Subclass of Polygon representing a Pentagon.
    """
    def __init__(self, side=0):
        """
        Initialize a Pentagon with a specified side length.

        :param side: Length of each side of the pentagon.
        """
        super().__init__()
        self.__side = side

    def perimeter(self):
        """
        Calculate the perimeter of the pentagon.

        :return: Perimeter of the pentagon.
        """
        return self.__side * 5

    def area(self):
        """
        Calculate the area of the pentagon using the formula for a regular pentagon.

        :return: Area of the pentagon.
        """
        return 0.25 * sqrt(5 * (5 + 2 * sqrt(5))) * pow(self.__side, 2)

    def draw(self):
        """
        Draw the pentagon using the Turtle graphics library.
        """
        for i in range(5):
            forward(self.__side + 100)
            left(72)


# Define a subclass Hexagon that inherits from Polygon.
class Hexagon(Polygon):
    """
    Subclass of Polygon representing a Hexagon.
    """
    def __init__(self, side=0):
        """
        Initialize a Hexagon with a specified side length.

        :param side: Length of each side of the hexagon.
        """
        super().__init__()
        self.__side = side

    def perimeter(self):
        """
        Calculate the perimeter of the hexagon.

        :return: Perimeter of the hexagon.
        """
        return self.__side * 6

    def area(self):
        """
        Calculate the area of the hexagon using the formula for a regular hexagon.

        :return: Area of the hexagon.
        """
        return (3 * sqrt(3) / 2) * pow(self.__side, 2)

    def draw(self):
        """
        Draw the hexagon using the Turtle graphics library.
        """
        for i in range(6):
            forward(self.__side + 100)
            left(60)


# Define a subclass Octagon that inherits from Polygon.
class Octagon(Polygon):
    """
    Subclass of Polygon representing an Octagon.
    """
    def __init__(self, side=0):
        """
        Initialize an Octagon with a specified side length.

        :param side: Length of each side of the octagon.
        """
        super().__init__()
        self.__side = side

    def perimeter(self):
        """
        Calculate the perimeter of the octagon.

        :return: Perimeter of the octagon.
        """
        return self.__side * 8

    def area(self):
        """
        Calculate the area of the octagon using a formula specific to octagons.

        :return: Area of the octagon.
        """
        return 2 * (1 + sqrt(2)) * pow(self.__side, 2)

    def draw(self):
        """
        Draw the octagon using the Turtle graphics library.
        """
        for i in range(8):
            forward(self.__side + 100)
            left(45)
