#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            count = count + 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return (count)
