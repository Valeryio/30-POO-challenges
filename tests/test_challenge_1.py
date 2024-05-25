#!/usr/bin/env python3

"""
    This is the test file for the module 1 of this challenge
"""

import unittest
from challenges.challenge_1 import Biscuit


class TestBiscuit(unittest.TestCase):
    """
        This is the test file for the biscuit's class
    """

    def setUp(self):
        """
            This is the setUp property for all the rest of
            our class
        """
        self.chichock = Biscuit("chichock cookie", "circle");
    
    def test_attributes(self):
        self.assertEqual(self.chichock.name, "chichock cookie")
        self.assertEqual(self.chichock.form, "circle")

    def test_setters(self):
        # Simple test to check if the right values have been updated
        self.chichock.name = "salted cookie"
        self.chichock.form = "square"

        self.assertEqual(self.chichock.name, "salted cookie")
        self.assertEqual(self.chichock.form, "square")

        # Simple test to check if the right values have been updated
        with self.assertRaises(TypeError) as context:
            self.chichock.name = True
            self.chichock.form = 0

        error_message = "The new attribute is not a string"
        self.assertEqual(str(context.exception), error_message)

    def test_method_cooked(self):
        result = "This chichock cookie have been cooked in a shape of circle"
        self.assertEqual(self.chichock.cooked(), result)
