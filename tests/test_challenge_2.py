#!/usr/bin/env python3

"""
    This is the test module of the class ...
"""

import unittest
from challenges.challenge_2 import Book


class TestBook(unittes.TestCase):
    """
        This is the class that will test the book class
    """

    def setUp(self):
        self.f_book = Book("Limitless", "Jim Kwik", "40$")
    

    def test_attributes(self):
        """
            This method tests all the attributes of the class
        """
