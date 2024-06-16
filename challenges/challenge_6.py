#!/usr/bin/env python3

# This is the module of the class Student

class Student(Person):
    """This is the class Student, a child of the class Person

     Attributes:
        @level: (integer), the level of the scolarship of the
                Child
    """
    def __init__(self, name, age, gender, level):
        """This is the constructor calling the parent's constructor"""
        super.__init__(name, age, gender)
        self.level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if type(level) is not str:
            raise TypeError("The level should be an integer")
