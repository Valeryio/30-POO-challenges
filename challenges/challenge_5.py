#!/usr/bin/env python3

# This module contains the class person

class Person():
    """
        This is the class of a person

        Attributes:
            @name: (str), the name of the person
            @gender: (str), the gender of the person
            @age: (int), the age of the person
    """

    def __init__(self, name, age, gender):
        """This is the constructor of the Person's class"""
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError("The name should be a string")
        else:
            self.__name = name

    @age.setter
    def age(self, age):
        if type(age) is not int:
            raise TypeError("The age should be an integer")
        elif age < 0:
            raise TypeError("An age cannot start below 0")
        else:
            self.__age = age

    @gender.setter
    def gender(self, gender):
        if type(gender) is not str:
            raise TypeError("The gender should be a string")
        else:
            self.__gender = gender
