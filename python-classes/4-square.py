#!/usr/bin/python3
"""define a square"""


class Square:
    '''
    define a square
        has a private instance att: size
    '''

    def __init__(self, size=0):
        ''' init size '''
        self.__size = size

        @property
        def size(self):
            ''' getter method '''
            return self.__size

        @size.setter
        def size(self, value):
            ''' setter method '''

            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValuError("size must be >= 0")
            self.__size = value

            def area(self):
                square_area = self.__size ** 2
                return square_area
