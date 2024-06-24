#!/usr/bin/env python3

# This is the test suite for the class PasswordGen

import unittest
from challenges.password_gen import PasswordGen

class TestPasswordGen():
    """This is the test class for PasswordGen
    Attributes:
        @:
    """

    def setUp(self):
        """This method sets up the variables for the test class"""
        self.passwd = PasswordGen(8, True, True, True, True)

    def test_include_uppercase(self):
        """This test checks the method include_uppercase()"""
        pass

    def test_include_lowercase(self):
        """This test checks the method include_lowercase()"""
        pass

    def test_include_digit(self):
        """This test checks the method include_digit()"""
        pass

    def test_include_special_char(self):
        """This test checks the method include_special_char()"""
        pass

    def test_generate_passwd(self)
        """This test checks the method generate_passwd()"""
        pass

    def evaluate_passwd(self):
        """This test checks the method evaluate_passwd()"""
        pass

    def save_passwd(self):
        """This test checks the method save_passwd()"""
        pass

    def read_passwd(self):
        """This test checks the method read_passwd()"""
        pass
