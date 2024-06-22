#!/usr/bin/env python3

# This is the test module for the vector 4d

import unittest
from challenges.vector_4d import Vector4D

class TestVector4D(unittest.TestCase):
    """This is the test class for the vector 4D"""
    
    def setUp(self):
        """This test setup the different attributes for the class"""
        self.first_vec = Vector4D(2, 4, 1, 9)
        self.second_vec = Vector4D(1, 3, 4, 5)
        self.third_vec = Vector4D()

    def test_attributes(self):
        """This test checks if all attributes of the class Vector4D are
        valid"""
        self.assertEqual(self.first_vec.u, 2)
        self.assertEqual(self.first_vec.v, 4)
        self.assertEqual(self.first_vec.x, 1)
        self.assertEqual(self.first_vec.y, 9)

    def test_add(self):
        """This test checks the __add__() magic method of Vector4D"""
        self.third_vec = self.first_vec + self.second_vec

        self.assertEqual(self.third_vec.u, 3)
        self.assertEqual(self.third_vec.v, 7)
        self.assertEqual(self.third_vec.x, 5)
        self.assertEqual(self.third_vec.y, 14)

    def test_sub(self):
        """This test checks the __sub__() magic method of the Vector4D"""
        sub_vector = self.first_vec - Vector4D(1, 1, 1, 1)
        self.assertEqual(sub_vector.u, 1)
        self.assertEqual(sub_vector.v, 3)
        self.assertEqual(sub_vector.x, 0)
        self.assertEqual(sub_vector.y, 8)

    def test_mul(self):
        """This test checks the __mul__() magic method of the Vector4D"""

        mul_vector = self.first_vec * self.second_vec
        
        self.assertEqual(mul_vector.u, 2)
        self.assertEqual(mul_vector.v, 12)
        self.assertEqual(mul_vector.x, 4)
        self.assertEqual(mul_vector.y, 45)

    def test_truediv(self):
        """This test checks the __truediv__() magic method of the Vector4D"""

        truediv_vector = self.second_vec / 2

        self.assertEqual(truediv_vector.u, 0.5)
        self.assertEqual(truediv_vector.v, 1.5)
        self.assertEqual(truediv_vector.x, 2)
        self.assertEqual(truediv_vector.y, 2.5)

        with self.assertRaises(ZeroDivisionError) as context:
            result = self.second_vec / Vector4D(0, 0, 4, 5)
