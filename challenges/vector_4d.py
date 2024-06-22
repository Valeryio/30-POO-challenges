#!/usr/bin/env node

# This is the module of the class vector_4d

class Vector4D():
    """This is the class for the vector 4d

    Attributes:
        @x : (int) absissa
        @y : (int) ordinate
        @u : (int) depth
        @v : (int) aka
    """

    def __init__(self, u=0, v=0, x=0, y=0):
        """This is the constructor of the class"""
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def __eq__(self, other):

    def __add__(self, other):
        """This is an overwriting of the add magic metho"""
        if type(other) is int:
            new_vector = Vector4D(self.u * other, self.v * other, \
                    self.x * other, self.y * other)
            return new_vector
        else if type(other) is Vector4D:
            new_vector = Vector4D(self.u * other.u, self.v * other.v), \
                    self.x * other.x, self.y * other.y)
            return new_vector

    @property
    def u(self):
        return self.__u

    @property
    def v(self):
        return self.__v

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @u.setter
    def u(self, u):
        if type(u) is not int:
            raise TypeError("The value should be an integer")
        elif u is None:
            self.__u = 0
        else:
            self.__u = u

    @u.setter
    def v(self, v):
        if type(v) is not int:
            raise TypeError("The value should be an integer")
        elif v is None:
            self.__v = 0
        else:
            self.__v = v

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("The value should be an integer")
        elif x is None:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("The value should be an integer")
        elif y is None:
            self.__y = 0
        else:
            self.__y = y
