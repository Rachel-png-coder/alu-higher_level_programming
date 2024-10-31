#!/usr/bin/python3
"""define a square"""


class Square:
    '''
    define a square
        has a private instance att: size
    '''

    def __init__(self, size=0):
        ''' init size '''
        elf.__size = size

        @property
        def size(self):
            "returns the size att"
            return self.__size

        @size.setter
        def size(self, size):
            '''asign the size to the size att'''
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValuError("size must be >= 0")
            self.__size = size

            def area(self):
                square_area = self.__size ** 2
                return square_area
