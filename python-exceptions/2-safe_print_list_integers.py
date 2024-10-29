#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p = y = 0
    while p < x:
        try:
            print("{:d}".format(my_list=[p]), end="")
            y += 1
        except (ValueError, TypeError):
            continue
        finally:
            p += 1
            print("")
            return ("y")
