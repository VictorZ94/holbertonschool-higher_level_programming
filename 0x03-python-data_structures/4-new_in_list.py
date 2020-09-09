#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Newlist = list.copy(my_list)
    Newlist[idx] = element
    return (Newlist)
