#!/usr/bin/python3
"""
    defines a rectangle by
"""

class Rectangle:
    """
        rectangle
    """

    def __init__(self, width=0, height=0):
        """ initialises a rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method """
        if not isinstance(value, int):
             raise TypeError("width must be an integer")
         if value < 0:
              raise ValueError("width must be >= 0")
          self.__width = value

    @height.setter
    def height(self, value):
        """ getter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

def area(self):
    """ Return the area of a rectangle """
    return self.__width * self.__height

def perimeter(self):
    """ Return perimetr of a rectangle """
    if self.__width == 0 or self.__height == 0:
        return 0
    else:
        return (2 * self.__width) + (2 * self.__height)

