#!/usr/bin/python3
def no_c(my_string):
    Newstring = removeChar(my_string, 'C')
    Newstring = removeChar(Newstring, 'c')
    return (Newstring)


def removeChar(s, c):
    counts = s.count(c)
    s = list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = ''.join(s)
    return(s)
