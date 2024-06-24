#!/usr/bin/env python3

# This is the test suite for the Calculator class

import unittest
from challenges.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """This is the test class of Calculator"""

    def setUp(self):
        """This method sets up the different variables
        of the class"""
        self.calculator_one = Calculator(4)

    def test_attributes(self):
        """This test checks if the attributes of Calculator
        are valid"""
        self.assertEqual(self.calculator_one.variable, x)

    def test_sum(self):
        """This test checks for the sum method of Calculator"""
        pass

    def test_mul(self):
        """This test checks for the mul method of Calculator"""
        pass

    def test_div(self):
        """This test checks for the div method of Calculator"""
        pass
