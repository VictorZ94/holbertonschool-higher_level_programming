#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0 and idx <= len(my_list):
        i = 0
        while i < idx:
            i += 1
            continue
        return (my_list[i])
    else:
        return ('None')
