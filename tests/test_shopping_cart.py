#!/usr/bin/env python3

# This is the test suite for the module of the shopping cart Class

import sys
import unittest
from io import StringIO
from challenges.article import Article
from challenges.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    """This is the test class
    Attributes:
        @cart_food: (object), a food shopping cart
        @cart_clothes: (object), a clothes shopping cart
    """

    def setUp(self):
        """This method sets up all the needed attributes for the
        tests"""
        self.cart_food = ShoppingCart("Banana", 12, 2.5)
        self.cart_clothes = ShoppingCart("Jacket", 2, 1000)

    def test_attributes(self):
        """This test checks if all the attributes have the right values"""

        self.assertEqual(self.cart_food.name, "Banana")
        self.assertEqual(self.cart_food.quantity, 12)
        self.assertEqual(self.cart_food.unit_price, 1000)

        with self.assertRaise(TypeError) as context
            test_variable = ShoppingCart("Banana", 's', 'o')

    def test__str__(self):
        """This test checks the __str__() magic method"""
        result = "[(\"Banana\", 12, 2.5), (\"Galaxy A22\", 1, 230)]\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.cart_food.list_articles()
        sys.stdout = sys.__stdout__

    def test_add_article(self):
        """This test checks the method add_article()"""
        new_article = Article("Audemars Piguet", "400000")
        self.cart_clothes.add_article(new_article)

        self.assertEqual(self.cart_clothes.article[new_article.name],\
                new_article)

    def test_remove_article(self):
        """This test removes an article from a shopping cart"""
        self.cart_clothes.remove_article("Audemars Piguet")
        with self.assertRaises(KeyError):
            tmp_result = self.cart_clothes.article["Audemars Piguet"]


    def test_get_shopping_cost(self):
        """This test checks the get_shopping_cost() method"""
        new_article = Article("Galaxy A22", "200")
        self.cart_clothes.add_article(new_article)
        
        self.assertEqual(self.cart_clothes.get_shopping_cost(), 230)

    def test_list_articles(self):
        """This test checks the list_articles() method"""
        result = "[\"Banana, 12, 2.5\", \"Galaxy A22\"]\n"
        output_obj = StringIO()
        sys.stdout = output_obj

        self.cart_food.list_articles()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_obj.getvalue(), result)

    def test_get_total_cost(self):
        """This test checks the get_total_cost() method"""
        result = 30
        self.assertEqual(self.cart_food.get_total_cost("Banana"),\
                result)

    def test_get_quantity(self):
        """This test checks the get_quantity() method"""
        result = 12
        self.assertEqual(self.cart_food.get_quantity("Banana"), 12)

    def test_count_distinct_article(self):
        """This test checks the number of articles in the shopping
        cart"""
        self.assertEqual(self.cart_food.count_disinct_article(), 2)
