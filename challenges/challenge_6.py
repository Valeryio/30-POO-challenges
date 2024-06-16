#!/usr/bin/env python3

# This is the module of the class Student
from . import Person

class Student(Person):
    """This is the class Student, a child of the class Person

     Attributes:
        @level: (integer), the level of the scolarship of the
                Child
    """
    def __init__(self, name, age, gender, level):
        """This is the constructor calling the parent's constructor"""
        super().__init__(name, age, gender)
        self.level = level

    def __repr__(self):
        """This method is the repr of the child"""


    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if type(level) is not str:
            raise TypeError("The level should be an integer")
        else:
            self.__level = level

    def registered_student(self):
        """This method prints a child"""

        if students is None:
            pass
        else:

