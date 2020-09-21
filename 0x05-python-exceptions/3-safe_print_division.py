#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        res = None
        return (res)
    finally:
        print("Inside result: {}".format(res))
