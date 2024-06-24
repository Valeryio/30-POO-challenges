#!/usr/bin/env python3

# This is the test suite for the Calculator class

import unittest
from challenges.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """This is the test class of Calculator"""

    def setUp(self):
        """This method sets up the different variables
        of the class"""
        pass

    def test_attributes(self):
        """This test checks if the attributes of Calculator
        are valid"""
        pass

    def test_sum(self):
        """This test checks for the sum method of Calculator"""
        self.assertEqual(Calculator.sum(1, 2), 3)
        with self.assertRaises(TypeError) as context:
            result = Calculator.div(4 / '0')

    def test_mul(self):
        """This test checks for the mul method of Calculator"""
        self.assertEqual(Calculator.mul(1, 2), 2)
        with self.assertRaises(TypeError) as context:
            result = Calculator.div(4 / '0')

    def test_div(self):
        """This test checks for the div method of Calculator"""
        self.assertEqual(Calculator.div(1, 2), 0.5)
        with self.assertRaises(TypeError) as context:
            result = Calculator.div(4 / '0')

        with self.assertRaises(ZeroDivisionError) as context:
            result = Calculator.div(4 / 0)
