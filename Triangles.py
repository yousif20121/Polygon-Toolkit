# Import necessary modules.
from Polygon import *
from math import *
from turtle import *


# Define a Triangle class that inherits from the Polygon class.
class Triangle(Polygon):
    """
    Subclass of Polygon representing a Triangle.
    """
    def __init__(self, side_1=0, side_2=0, side_3=0,
                 base=0, height=0,
                 angle_1=0, angle_2=0):
        """
        Initialize a Triangle with various properties.

        :param side_1: Length of the first side.
        :param side_2: Length of the second side.
        :param side_3: Length of the third side.
        :param base: Length of the base.
        :param height: Height of the triangle.
        :param angle_1: First angle of the triangle.
        :param angle_2: Second angle of the triangle.
        """
        super().__init__()
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3
        self.__base = base
        self.__height = height
        self.__angle_1 = angle_1
        self.__angle_2 = angle_2

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.

        :return: Perimeter of the triangle.
        """
        return self.__side_1 + self.__side_2 + self.__side_3

    def area(self):
        """
        Calculate the area of the triangle using the base and height.

        :return: Area of the triangle.
        """
        return 0.5 * self.__base * self.__height

    def draw(self):
        """
        Draw the triangle using the Turtle graphics library.
        """
        forward(self.__side_1 + 100)
        left(180 - self.__angle_1)
        forward(self.__side_2 + 100)
        left(180 - self.__angle_2)
        forward(self.__side_3 + 100)


# Define a subclass IsoTriangle that inherits from Triangle.
class IsoTriangle(Triangle):
    """
    Subclass of Triangle representing an Isosceles Triangle.
    """
    def __init__(self, side_1_rep=0, side_2=0,
                 base=0, height=0,
                 angle_1=0):
        """
        Initialize an Isosceles Triangle with various properties.

        :param side_1_rep: Length of the repeating side.
        :param side_2: Length of the second side.
        :param base: Length of the base.
        :param height: Height of the triangle.
        :param angle_1: Angle of the triangle.
        """
        super().__init__()
        self.__side_1_rep = side_1_rep
        self.__side_2 = side_2
        self.__base = base
        self.__height = height
        self.__angle_1 = angle_1

    def perimeter(self):
        """
        Calculate the perimeter of the isosceles triangle.

        :return: Perimeter of the isosceles triangle.
        """
        return self.__side_1_rep * 2 + self.__side_2

    def draw(self):
        """
        Draw the isosceles triangle using the Turtle graphics library.
        """
        forward(self.__side_1_rep + 100)
        left(180 - self.__angle_1)
        forward(self.__side_1_rep + 100)
        left(180 - self.__angle_1)
        forward(self.__side_2 + 100)


# Define a subclass EquiTriangle that inherits from Triangle.
class EquiTriangle(Triangle):
    """
    Subclass of Triangle representing an Equilateral Triangle.
    """
    def __init__(self, side):
        """
        Initialize an Equilateral Triangle with a specified side length.

        :param side: Length of each side of the equilateral triangle.
        """
        super().__init__()
        self.__side = side

    def perimeter(self):
        """
        Calculate the perimeter of the equilateral triangle.

        :return: Perimeter of the equilateral triangle.
        """
        return 3 * self.__side

    def area(self):
        """
        Calculate the area of the equilateral triangle using its side length.

        :return: Area of the equilateral triangle.
        """
        return (sqrt(3)/4) * pow(self.__side, 2)

    def draw(self):
        """
        Draw the equilateral triangle using the Turtle graphics library.
        """
        for i in range(3):
            forward(self.__side + 100)
            left(120)
