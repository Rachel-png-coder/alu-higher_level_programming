#!/usr/bin/python3
""" class MyList that inherits from list """


class Mylist(list):
    """ implement sorted print """

    def print_sorted(self):
        """ print a list on sorted ascending order """
        print(sorted(self))
