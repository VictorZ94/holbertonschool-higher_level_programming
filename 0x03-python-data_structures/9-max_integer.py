#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return (None)
    list.sort(my_list)
    return (my_list[-1])
