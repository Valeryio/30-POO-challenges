#!/usr/bin/python3

# This module contains only one class, that is for the biscuit

class Biscuit:
    """
        This is the class of a biscuit

        Attributes:
            name (string): the name of the biscuit
            form (string): the shape of the biscuit
    """

    def __init__(self, name, form):
        self.__name = name
        self.__form = form

    @property
    def name(self):
        """
            This method is a getter of the name attribute
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
            This method is a setter for the name attribute
            Args:
                value (string): the new value of the name
        """
        if isinstance(value, str):
            self.__name = value
        else:
            print("The new arg is not a string")

    @property
    def form(self):
        """
            This method is a getter for the form attribute
        """
        return self.__form

    @form.setter
    def form(self, form):
        """
            This is a setter for the form attribute
        """
        if isinstance(form, str):
            self.__form = form
        else:
            print("The new attribute is not a string")

    def cuir(self):
        print("This", self.__name, "have been")
