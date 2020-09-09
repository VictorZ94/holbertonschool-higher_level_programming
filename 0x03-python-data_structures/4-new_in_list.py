#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        Newlist = list.copy(my_list)
        Newlist[idx] = element
        return (Newlist)
    else:
        return ('None')
