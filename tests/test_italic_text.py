#!/usr/bin env python3

# This the test suite for the text class

import sys
import unittest
from io import StringIO
from challenges.italic_text import ItalicText

class TestItalicText(unittest.TestCase):
    """This is the test class for the ItalicText
    Attributes:
        @peterson_quote: (ItalicText Object)
        @david_g_quote: (ItalicText Object)
    """

    def setUp(self):
        """This method sets up all the needed object
       for the tests"""
        self.peterson_quote = ItalicText("Une femme n'est pas un objet")
        self.david_g_quote = ItalicText("Stay hard!")

    def test_attributes(self):
        """This test checks if the attributes of Text class are valid""" 
        quote = "Une femme n'est pas un objet"
        self.assertEqual(self.peterson_quote.sentence, quote)

    def test_show_text(self):
        """This test checks the show_text() method of BoldText"""
        result = "_Stay hard!_\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.david_g_quote.show_text()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_obj.getvalue(), result)
