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
        return self.__class__ == other.__class__

    def __add__(self, other):
        """This is an overloading of the add magic method"""
        if type(other) is int:
            new_vector = Vector4D(self.u * other, self.v * other, \
                    self.x * other, self.y * other)
            return new_vector
        elif type(other) is Vector4D:
            new_vector = Vector4D(self.u + other.u, self.v + other.v, \
                    self.x + other.x, self.y + other.y)
            return new_vector

    def __sub__(self, other):
        """This is an overloading of the sub magic method"""
        if type(other) is int:
            new_vector = Vector4D(self.u - other, self.v - other, \
                    self.x - other, self.y - other)
            return new_vector
        elif type(other) is Vector4D:
            new_vector = Vector4D(self.u - other.u, self.v - other.v, \
                    self.x - other.x, self.y - other.y)
            return new_vector

    def __mul__(self, other):
        """This is an overloading of the mul magic method"""
        if type(other) is int:
            new_vector = Vector4D(self.u * other, self.v * other, \
                    self.x * other, self.y * other)
            return new_vector
        elif type(other) is Vector4D:
            new_vector = Vector4D(self.u * other.u, self.v * other.v, \
                    self.x * other.x, self.y * other.y)
            return new_vector

    def __truediv__(self, other):
        """This is an overloading of the add magic method"""
        if type(other) is int and other != 0:
            new_vector = Vector4D(self.u / other, self.v / other, \
                    self.x / other, self.y / other)
            return new_vector
        elif type(other) is Vector4D:
            if 0 in other.__dict__.values():
                raise ZeroDivisionError()
            else:
                new_vector = Vector4D(self.u / other.u, self.v / other.v, \
                    self.x / other.x, self.y / other.y)
                return new_vector

    def __repr__(self):
        return str(self.__dict__)

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
        if type(u) not in (int, float):
            raise TypeError("The value should be an integer")
        elif u is None:
            self.__u = 0
        else:
            self.__u = u

    @v.setter
    def v(self, v):
        if type(v) not in (int, float):
            raise TypeError("The value should be an integer")
        elif v is None:
            self.__v = 0
        else:
            self.__v = v

    @x.setter
    def x(self, x):
        if type(x) not in (int, float):
            raise TypeError("The value should be an integer")
        elif x is None:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) not in (int, float):
            raise TypeError("The value should be an integer")
        elif y is None:
            self.__y = 0
        else:
            self.__y = y
