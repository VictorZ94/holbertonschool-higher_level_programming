#!/usr/bin/python3
"""Declare new class
"""


class Student:
    """Doc"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        dic = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic

    def reload_from_json(self, json):
        self.__dict__.clear()
        for iter in json:
            self.__dict__[iter] = json[iter]
