#!/usr/bin/env python3

# This file contains the class of a circle

class Circle():
    """
        This is a circle's

        Attributes:
            @name : (str), the name of the circle
            @x : (int), the x position of the circle
            @y : (int), the y position of the circle
            @radius : (int), the radius of the circle
    """

    def __init__(self, name, x, y, radius):
        """Initialise the object"""
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def name(self):
        """This is the getter of the attribute name"""
        return self.__name

    @property
    def x(self):
        """This is the getter of the attribute x"""
        return self.__x

    @property
    def y(self):
        """This is the getter of the attribute y"""
        return self.__y

    @property
    def radius(self):
        """This is the getter of the attribute radius"""
        return self.__radius
    
    @name.setter
    def name(self, name):
        """This is the setter of the attribute name"""
        self.__name = name

    @x.setter
    def x(self, x):
        """This is the setter of the attribute x"""
        self.__x = x

    @y.setter
    def y(self, y):
        """This is the setter of the attribute y"""
        self.__y = y

    @radius.setter
    def radius(self, radius):
        """This is the setter of the attribute radius"""
        self.__radius = radius
    
    def perimeter(self):
        """This method returns the perimeter of the circle"""
        return self.__radius * 4

    def area(self):
        """This method returns the area of the circle"""
        return self.__radius * self.__radius

    def get_properties(self):
        """This method prints the attributes of the circle"""
        print(f"{self.__name}({self.__x}, {self.__y})(Radius: \
{self.__radius})")
