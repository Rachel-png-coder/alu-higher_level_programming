#!/usr/bin/python3
"""defines a square """

Class Square:
    """ defines a square """

    def __init__(self, size=0):
        """ initialises a square with size """
        self.__size = size

        @property
        def size(self):
            """ getter method """
            return self.__size
        
        @size.setter
        def size(self, value):
            """ setter method """

            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                ValueError(""size must be an integer")
                self.__size = size

        def area(self):
            """ Return the area of a square """
            return(self.__size * self.__size)

        def my_print(self):
            """ prints a square with the character # """
             if self.__size == 0:
                print("")
             for x in range(self.__size):
             print("#", end="")
             print()
