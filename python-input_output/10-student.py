#!/usr/bin/python3
"""defines a student by: (based on 9-student.py)"""


class Student:
    """Defines a Student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student.

        Args:
            attrs (list of str): List of attributes to include.

        Returns:
            dict: Dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)

        return student_dict
