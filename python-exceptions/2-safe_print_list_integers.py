#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p = 0
    for p in range (x):
        try:
            print("{:d}".format(my_list[p]), end="")
        except (ValueError, TypeError):
            pass
        else:
            p += 1
    print()
    return (p)
