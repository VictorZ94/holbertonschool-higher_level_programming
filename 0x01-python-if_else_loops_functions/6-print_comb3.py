#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j and j > i and j < 9:
            print("{}{}".format(i, j), end=", ")
    if i == 8 and j == 9:
        print("{}{}".format(i, j))
