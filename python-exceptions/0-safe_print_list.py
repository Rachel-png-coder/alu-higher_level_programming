#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    v = 0
    for v in range(x):
        try:
            print("{}".format(my_list[v]), end="")
        except IndexError:
            break
        v += 1
    print("")
    return (v)
