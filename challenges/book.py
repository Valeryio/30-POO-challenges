#!/usr/bin/env python3

"""
    This module contains the class Book
"""


class Book():
    """
        This is the class book
        Attributes:
            devise (string): the device of the money that will be used
            name (string): the name of the book
            price (int): the price of the book
    """
    devise = "$"

    def __init__(self, name, author, price):
        """
            This is the constructor of the function

            Arguments:
                name (string): the name of the book
                author (string): the author of the book
                price (int): the author of the book
        """
        self.name = name
        self.author = author
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("The name you given is not the right type")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self.__author = value
        else:
            raise TypeError("The author you given is not the right type")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, int):
            self.__price = value
        else:
            raise TypeError("The price you given is not the right type")

    def inform(self):
        print(f"Book {self.__name}, written by {self.__author} :: COST :\
 {self.price}")
