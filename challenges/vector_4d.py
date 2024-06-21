#!/usr/bin/env node

# This is the module of the class vector_4d

class Vector4D():
    """This is the class for the vector 4d

    Attributes:
        @x : (int)
        @y : (int)
        @u : (int)
        @v : (int)
    """

    def __init__(self, u=0, v=0, x=0, y=0):
        """This is the constructor of the class"""
        self.u = u
        self.v = v
        self.x = x
        self.y = y

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
        else:
            self.__u = u

    @u.setter
    def v(self, v):
        if type(v) is not int:
            raise TypeError("The value should be an integer")
        else:
            self.__v = v

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("The value should be an integer")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("The value should be an integer")
        else:
            self.__y = y
