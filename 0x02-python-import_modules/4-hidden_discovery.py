#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for nombres in dir(hidden_4):
        if not nombres.startswith('__'):
            print(nombres)
