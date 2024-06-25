#!/usr/bin/env python3

# This is the module of the class Article


class Article():
    """This is the class article
    Attributes:
        @name: (str), the name of the article
        @price: (int), the price of the article
    """

    def __init__(self, name, price):
        """Inits the Article with name and price"""
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.name}, {self.price})"

    @property
    def name(self):
        """Returns the name of the Article"""
        return self.__name

    @property
    def price(self):
        """Returns the price of the Article"""
        return self.__price

    @name.setter
    def name(self, name):
        """Sets the name attribute"""
        if type(name) is not str:
            raise TypeError()
        else:
            self.__name = name

    @price.setter
    def price(self, price):
        """Sets the price attribute"""
        if type(price) not in (int, float):
            raise TypeError()
        else:
            self.__price = price
