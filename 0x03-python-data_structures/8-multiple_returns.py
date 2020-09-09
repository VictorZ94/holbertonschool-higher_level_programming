#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        Newtuple = (0, None)
    else:
        Newtuple = (len(sentence), sentence[0])
    return Newtuple
