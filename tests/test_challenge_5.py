#!/usr/bin/env python3

"""
    This is the test module of the class Person
"""

import unittest
from challenges.challenge_5 import Person


class TestPerson(unittest.TestCase):
    """This is the test class of the Person"""

    def setUp(self):
        """This method sets up the different attributes of the class"""
        self.linson = Person("Linson", 20, "male")

    def test_attributes(self):
        """This method tests all the different attributes of the class
        person"""
        self.assertEqual(self.linson.name, "Linson")
        self.assertEqual(self.linson.age, 20)
        self.assertEqual(self.linson.gender, "male")

        with self.assertRaises(TypeError) as context:
            example = Person(4, 9, "male")
        self.assertEqual(str(context.exception), "The name should be a \\
string")

        with self.assertRaises(TypeError) as context:
            example = Person("Kaleb", "p", "male")
        self.assertEqual(str(context.exception), "The age should be an \\
integer")

        with self.assertRaises(TypeError) as context:
            example = Person("Kaleb", -9, "male")
        self.assertEqual(str(context.exception), "An age cannot start below\\
0")

        with self.assertRaises(TypeError) as context:
            example = Person("Claud", 9, 4)
        self.assertEqual(str(context.exception), "The gender should be a \\
string")

    def test_introduce_yourself(self):
        """This method test the method introduce_yourself of the class PErson"""
        intro = f"""My name is {self.linson.name}, I'm a {self.linson.gender}\\
of {self.linson.self.age}"""
        output_obj = StringIO()
        sys.stdout = output_obj

        linson.introduce_yourself()

        sys.stdout = sys.__stdout__
        self.assertEqal(output_obj.getvalue(), intro)

    def test_is_adult(self):
        """This test ensure that the is_adult() method is well written"""
        assertTrue(is_adult())
