"""
    Entity class should be coded here
"""

# Imports
import itertools


#


class Student:
    """
    The Student class
    """

    # id - unique
    identification = itertools.count(1)
    #

    def __init__(self, name="", group=-1):
        self.__name = name
        self.__group = group
        self.__id = next(self.identification)

    # Getters, setters

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self, name):
        self.__name = name

    @group.setter
    def group(self, group):
        self.__group = group

    @id.setter
    def id(self, student_id):
        self.__id = student_id

    # Print

    def print_student(self):
        # print("id:", self.__id, "; Name:", self.__name, "; Group:", self.__group)
        print(str(self.__id) + ".)", self.__name, self.__group)

    def __str__(self) -> str:
        return "({0}, {1}, {2})".format(self.__id, self.__name, self.__group)
