#!/usr/bin/python3
"""returns True if the object is an instance of, or if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """return true is isinstance is true else false"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
