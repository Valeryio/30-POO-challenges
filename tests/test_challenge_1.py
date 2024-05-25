#!/usr/bin/env python3

"""
    This is the test file for the module 1 of this challenge
"""

import unittest
import sys
from io import StringIO
from challenges.challenge_1 import Biscuit


class TestBiscuit(unittest.TestCase):
    """
        This is the test file for the biscuit's class
        Attributes:
            chichock (Biscuit): the object that we'll use for the tests
    """

    def setUp(self):
        """
            This is the setUp property for all the rest of
            our class
        """
        self.chichock = Biscuit("chichock cookie", "circle");
    
    def test_attributes(self):
        """
            This method tests all the attributes of the class
        """
        self.assertEqual(self.chichock.name, "chichock cookie")
        self.assertEqual(self.chichock.form, "circle")

    def test_setters(self):
        """
            This method tests the the setters for the right, and the
            non-authorized values
        """
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
        """
            This method tests the output of the method cooked
        """
        # create a new StringIO object and change the stdout to out new
        # IO object to capture the standard output until we restore it
        output_result = StringIO()
        sys.stdout = output_result

        # call the method to capture the output in output_result
        self.chichock.cooked()

        # close and restore stdout to the normal stream
        sys.stdout = sys.__stdout__

        result = "This chichock cookie have been cooked in a shape of circle\n"
        self.assertEqual(output_result.getvalue(), result)
