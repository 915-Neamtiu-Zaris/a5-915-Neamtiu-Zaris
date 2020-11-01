"""
    Service class includes functionalities for implementing program features
"""


# Imports (don't do it manually)
from domain.entity import Student
import random
import copy

#


class StudentService:

    __li_undo = []

    def __init__(self, validator):
        self.__entities = []
        self.__validator = validator

    def get_all_students(self):
        """
        For each student in the list of students, make a separate list containing the
        student information, and then return a list of all the lists.
        :return: A list of lists containing each of the students' information.
        """
        # return [[student.id, student.name, student.group] for student in self.__entities]
        return [student for student in self.__entities]

    def generate_students(self):
        """
        Adds 10 random students to the entities list.
        :return:
        """
        li_names = ["Zamfira", "Alexandra", "Bianca", "Paraschiva", "Teresa", "Victoria", "Zenobia", "Zoe",
                    "Viorica", "Simona", "Abel", "Anghel", "Bernard", "Bogdan", "Cristian", "Constantin",
                    "Casian", "Darius", "Dorin", "Emil"]

        len_names = len(li_names)

        for nr in range(0, 10):
            name_index = random.randint(0, len_names - 1)
            group = random.randint(900, 915)
            self.add_student(li_names[name_index], group)

    def add_student(self, name, group):
        """
        Adds a student to the students list (entities).
        :param name: The student name
        :param group: The student group
        :return:
        """
        # Once the list is generated completely, we want to remember
        # what all of its states before performing operations, so we can undo.
        if len(self.__entities) >= 10:
            self.__li_undo.append(copy.deepcopy(self.__entities))

        s = Student(name, group)
        self.__validator.validate(s)
        self.__entities.append(s)

    def filter_students(self, group):
        """
        Removes all the students belonging to a certain group
        from the students list.
        :param group: The group of the students that will be removed.
        :return:
        """
        # We want to remember the states of the list before performing any changes,
        # so we can undo.
        self.__li_undo.append(copy.deepcopy(self.__entities))

        index = 0
        while index < len(self.__entities):
            if self.__entities[index].group == group:
                self.__entities.pop(index)
                index -= 1
            index += 1

    def undo(self):
        """
        Removes the effect of the last performed operation.
        """
        length = len(self.__li_undo)

        if length == 0:
            raise Exception("There have been no list changing operations performed, or you undid them all.")

        self.__entities = self.__li_undo[length - 1]
        self.__li_undo.pop()
