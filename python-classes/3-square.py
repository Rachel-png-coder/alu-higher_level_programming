#!/usr/bin/python3
"""defines a square """


class Square:
    '''
    defines a square
         has a private instance att: size
    '''

    def __init__(self, size=0):
        ''' init size '''
        if not isinstance(size, int):
            raise TpeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.size = size

    def area(self):
        square_area = self.size ** 2
        return square_area
