#!/usr/bin/python3
"""Class Base Father
"""
import json


class Base:
    """nb Objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or list_objs == []:
            Newlist = []
        else:
            Newlist = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])

        with open(cls.__name__ + ".json", "w") as myFile:
            myFile.write(Newlist)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        Newlist = []
        try:
            with open("{}.json".format(cls.__name__), mode="rt") as f:
                listtemp = cls.from_json_string(f.read())
        except:
            listtemp = []

        for iter in listtemp:
            Newlist.append(cls.create(**iter))
        return Newlist
