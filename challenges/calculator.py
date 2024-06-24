#!/usr/bin/env python3

# This is the module of the simple class calculator


class Calculator():
    """This is the class Calculator that have some beautiful
        static functions to use
    """

    def __init__(self):
        """This is a simple constructor for the class"""
        pass

    @staticmethod
    def sum(x, y):
        """This method computes the sum of a two number"""
        __class__.check_integer(x)
        __class__.check_integer(y)
        return x + y

    @staticmethod
    def mul(x, y):
        """This method computes the mul of a two number"""
        __class__.check_integer(x)
        __class__.check_integer(y)
        return x * y

    @staticmethod
    def div(x, y):
        __class__.check_integer(x)
        __class__.check_integer(y)
        if y == 0:
            raise ZeroDivisionError()
        else:
            return x / y

    @staticmethod
    def check_integer(x):
        """This method checks if a number is an integer or not"""
        if type(x) is not int:
            raise TypeError()
        else:
            return True
