#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                print("{}".format(i), end="")
                count = count + 1
    except IndexError:
        return (count)
    print()
    return (count)
