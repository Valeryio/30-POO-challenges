#!/usr/bin/env python3

"""
    This is the test module of the class Circle
"""

import sys
import unittest
from io import StringIO
from challenges.challenge_4 import Circle


class TestCircle(unittest.TestCase):
    """This is the test class of the class Circle"""

    def setUp(self):
        """This methods set up the different attributes of the test class"""
        self.simple_circle = Circle("O", 1, 1, 6)

    def test_attributes(self):
       """This method tests the differents attributes of the class Circle"""
       
       self.assertEqual(self.simple_circle.name, "O")
       self.assertEqual(self.simple_circle.x, 1)
       self.assertEqual(self.simple_circle.y, 1)
       self.assertEqual(self.simple_circle.radius, 6)

    def test_perimeter(self):
        """This methods tests the perimeter method of the class Circle"""
        
        perimeter = 24
        self.assertEqual(perimeter, self.simple_circle.perimeter())

    def test_area(self):
        """This methods tests the area method of the class Circle"""

        area = 36
        self.assertEqual(area, self.simple_circle.area())

    def test_get_properties(self):
        """This methods tests the get_properties() method of the class
        Circle"""

        result = f"""{self.simple_circle.name}({self.simple_circle.x},\
 {self.simple_circle.y})(Radius: {self.simple_circle.radius})\n"""

        output_obj = StringIO()
        sys.stdout = output_obj

        self.simple_circle.get_properties()

        sys.stdout = sys.__stdout__
        self.assertEqual(output_obj.getvalue(), result)
