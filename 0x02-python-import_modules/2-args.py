#!/usr/bin/python3
import sys
i = 1
args = sys.argv[1:]
print("{} arguments:".format(len(sys.argv) - 1))
for arguments in args:
    print("{}: {}".format(i, str(arguments)))
    i += 1
