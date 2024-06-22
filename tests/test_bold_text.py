#!/usr/bin env python3

# This the test suite for the text class

import sys
import unittest
from io import StringIO
from challenges.bold_text import BoldText

class TestBoldText(unittest.TestCase):
    """This is the test class for the BoldText
    Attributes:
        @peterson_quote: (BoldText Object)
        @david_g_quote: (BoldText Object)
    """

    def setUp(self):
        """This method sets up all the needed object
        for the tests"""
        self.peterson_quote = BoldText("Une femme n'est pas un objet")
        self.david_g_quote = BoldText("Stay hard!")

    def test_attributes(self):
        """This test checks if the attributes of BoldText
        class are valid""" 
        quote = "Une femme n'est pas un objet"
        self.assertEqual(self.peterson_quote.sentence, quote)

    def test_show_text(self):
        """This test checks the show_text() method of BoldText"""
        result = "**Stay hard!**\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.david_g_quote.show_text()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_obj.getvalue(), result)
