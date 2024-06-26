#!/usr/bin/env python3

"""
    This is the test module of the class Book
"""

import unittest
import sys
from io import StringIO
from challenges.book import Book


class TestBook(unittest.TestCase):
    """
        This is the class that will test the book class
    """

    def setUp(self):
        """
            This method set up the different methods that
            are used in this test_class
        """
        self.f_book = Book("Limitless", "Jim Kwik", 40)
    

    def test_attributes(self):
        """
            This method tests all the attributes of the class
        """
        self.assertEqual(self.f_book.name, "Limitless")
        self.assertEqual(self.f_book.author, "Jim Kwik")
        self.assertEqual(self.f_book.price, 40)


    def test_setters(self):
        """
            This method tests the setters of the attribute of the class
        """
        # self.f_book = Book("Start by the WHY", "Simon Sinek", 32)
        error_name = "The name you given is not the right type"
        error_author = "The author you given is not the right type"
        error_price = "The price you given is not the right type"

        with self.assertRaises(TypeError) as context:
           self.f_book.name = 6
        self.assertEqual(str(context.exception), error_name)

        with self.assertRaises(TypeError) as context:
           self.f_book.author = 6
        self.assertEqual(str(context.exception), error_author)

        with self.assertRaises(TypeError) as context:
           self.f_book.price = 's'
        self.assertEqual(str(context.exception), error_price)

    def test_inform(self):
        """
            This method tests the method infom() of the class Book
        """
        result = f"Book {self.f_book.name}, written by {self.f_book.author}\
 :: COST : {self.f_book.price}\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.f_book.inform()

        sys.stdout = sys.__stdout__
        self.assertEqual(output_obj.getvalue(), result)
