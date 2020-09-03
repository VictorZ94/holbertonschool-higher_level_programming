#!/usr/bin/python3
import sys
args = len(sys.argv) - 1
if args == 0:
    print("{} arguments.".format(args))
elif args == 1:
    print("{} argument.".format(args))
else:
    print("{} arguments:".format(args))
for index in range(len(sys.argv)):
    if (index == 0):
        continue
    print("{}: {}".format(index, sys.argv[index]))
