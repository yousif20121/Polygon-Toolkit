# Import necessary modules.
from Polygon import *
from math import *
from turtle import *


# Define a Quadrilateral class that inherits from the Polygon class.
class Quadrilateral(Polygon):
    """
    Subclass of Polygon representing a Quadrilateral.
    """
    def __init__(self, side_1=0, side_2=0, side_3=0, side_4=0,
                 angle_1=0, angle_2=0, angle_3=0):
        """
        Initialize a Quadrilateral with various properties.

        :param side_1: Length of the first side.
        :param side_2: Length of the second side.
        :param side_3: Length of the third side.
        :param side_4: Length of the fourth side.
        :param angle_1: First angle of the quadrilateral.
        :param angle_2: Second angle of the quadrilateral.
        :param angle_3: Third angle of the quadrilateral.
        """
        super().__init__()
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3
        self.__side_4 = side_4
        self.__angle_1 = angle_1
        self.__angle_2 = angle_2
        self.__angle_3 = angle_3

    def perimeter(self):
        """
        Calculate the perimeter of the quadrilateral.

        :return: Perimeter of the quadrilateral.
        """
        return self.__side_1 + self.__side_2 + self.__side_3 + self.__side_4

    def area(self):
        """
        Returns a message as the base class doesn't provide a specific area calculation.

        :return: A message indicating that more data is needed to calculate the area.
        """
        return f"Quadrilateral area: I need more data to do that"

    def draw(self):
        """
        Draw the quadrilateral using the Turtle graphics library.
        """
        forward(self.__side_1 + 100)
        left(self.__angle_1)
        forward(self.__side_2 + 100)
        left(self.__angle_2)
        forward(self.__side_3 + 100)
        left(self.__angle_3)
        forward(self.__side_4 + 100)


# Define a subclass Square that inherits from Quadrilateral.
class Square(Quadrilateral):
    """
    Subclass of Quadrilateral representing a Square.
    """
    def __init__(self, side=0):
        """
        Initialize a Square with a specified side length.

        :param side: Length of each side of the square.
        """
        super().__init__()
        self.__side = side

    def perimeter(self):
        """
        Calculate the perimeter of the square.

        :return: Perimeter of the square.
        """
        return self.__side * 4

    def area(self):
        """
        Calculate the area of the square using its side length.

        :return: Area of the square.
        """
        return pow(self.__side, 2)

    def draw(self):
        """
        Draw the square using the Turtle graphics library.
        """
        for i in range(4):
            forward(self.__side + 100)
            left(90)


# Define a subclass Rectangle that inherits from Quadrilateral.
class Rectangle(Quadrilateral):
    """
    Subclass of Quadrilateral representing a Rectangle.
    """
    def __init__(self, side_1=0, side_2=0):
        """
        Initialize a Rectangle with two specified side lengths.

        :param side_1: Length of the first side.
        :param side_2: Length of the second side.
        """
        super().__init__(side_1, side_2)
        self.__side_1 = side_1
        self.__side_2 = side_2

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: Perimeter of the rectangle.
        """
        return (self.__side_1 + self.__side_2) * 2

    def area(self):
        """
        Calculate the area of the rectangle using its side lengths.

        :return: Area of the rectangle.
        """
        return self.__side_1 * self.__side_2

    def draw(self):
        """
        Draw the rectangle using the Turtle graphics library.
        """
        for i in range(2):
            forward(self.__side_1 + 100)
            left(90)
            forward(self.__side_2 + 100)
            left(90)
