#!/usr/bin/python3
"""a function that returns the dictionary description with data structure"""


def class_to_json(obj):
    """for JSON serialization of an object:"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
