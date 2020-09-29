#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
try:
    say_my_name(14, 15)
except Exception as e:
    print(e)
try:
    say_my_name("Hello")
except Exception as e:
    print(e)
