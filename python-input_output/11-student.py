#!/usr/bin/python3
"""defines a student by: (based on 10-student.py)"""


class Student:
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dict representation."""
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)

        return student_dict

    def reload_from_json(self, json):
        """Replace attributes."""
        for key, value in json.items():
            setattr(self, key, value)
