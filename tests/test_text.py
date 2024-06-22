#!/usr/bin env python3

# This the test suite for the text class

import sys
import unittest
from io import StringIO
from challenges.text import Text

class TestText(unittest.TestCase):
    """This is the test class for the Text
    Attributes:
        @peterson_quote: (Text Object)
        @david_g_quote: (Text Object)
    """

    def setUp(self):
        """This method sets up all the needed object
        for the tests"""
        self.peterson_quote = Text("Une femme n'est pas un objet")
        self.david_g_quote = Text("Stay hard!")

    def test_attributes(self):
        """This test checks if the attributes of Text class are valid""" 
        quote = "Une femme n'est pas un objet"
        self.assertEqual(self.peterson_quote.sentence, quote)

    def test_show_text(self):
        """This test checks the show_text() method of Text"""
        result = "Stay hard!\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.david_g_quote.show_text()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_obj.getvalue(), result)
