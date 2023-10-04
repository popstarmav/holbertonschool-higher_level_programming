#!/usr/bin/python3
"""Base class module"""

import json
import os


class Base:
    """Base class for managing id attribute in future classes"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Initialize a new Base instance.

        Args:
            _id (int, optional): An integer ID. Defaults to None.
        """
        if _id is not None:
            self.id = _id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            ret = [cls.create(**d) for d in list_dicts]
        return ret

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance
