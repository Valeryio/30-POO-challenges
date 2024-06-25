#!/usr/bin/env python3

# This is the test suite for the module of the Article Class

import unittest
from challenges.article import Article


class TestArticle(unittest.TestCase):
    """This is the test class of Article
    Attributes:
        @banana: (object), an aliment
        @Jacket: (object), a clothe
    """

    def setUp(self):
        """This method sets up all the needed attributes for the
        tests"""
        self.banana = Article("Banana", 2.5)
        self.jacket = Article("Jacket", 1000)

    def test_attributes(self):
        """This test checks if all the attributes have the right values"""
        self.assertEqual(self.jacket.name, "Jacket")
        self.assertEqual(self.jacket.price, 1000)

        with self.assertRaises(TypeError) as context:
            test_variable = Article("Banana", 's')
