#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    New_list = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            New_list += [True]
        else:
            New_list += [False]
    return (New_list)
