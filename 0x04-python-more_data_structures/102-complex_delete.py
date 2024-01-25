#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for x, y in tmp.items():
        if value == y:
            my_dict.pop(x)
    return my_dict
