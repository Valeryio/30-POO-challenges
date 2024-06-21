#!/usr/bin/env python3

"""
    This is the test module of the class Student
"""
import sys
import unittest
from io import StringIO
from challenges.challenge_6 import Student


class TestStudent(unittest.TestCase):
    """This is the test suite for the class Student

    Attributes:
        @bigetty: (child object)
        @pacman: (child object)
        @student_list: (list), a list of child objects
    """

    def setUp(self):
        """This test sets up the different attributes for all the test
        suite"""
        self.bigetty = Student("Bigetty", 20, "male", "Terminal")
        self.pacman = Student("Erlyc", 38, "male", "Terminal")
        self.student_list = []
        self.student_list.append(self.bigetty)
        self.student_list.append(self.pacman)

    def test_attributes(self):
        """This test checks if all the attributes are well saved"""
        self.assertEqual(self.bigetty.age, 20)
        self.assertEqual(self.bigetty.gender, "male")
        self.assertEqual(self.bigetty.name, "Bigetty")
        self.assertEqual(self.bigetty.level, "Terminal")

        with self.assertRaises(TypeError) as context:
            test_attribute = Student("Melda", 20,"female", 5)
            self.assertEqual(str(context.content), "The level should be a integer")

    def test_registered_students(self):
        """This test checks the registered_students() method"""
        result = f"[(Bigetty, 20, male, Terminal)"\
                + f", (Erlyc, 38, male, Terminal)]\n"
        output_obj = StringIO()
        sys.stdout = output_obj
        
        # Execute the method and listening to the output
        self.bigetty.registered_students(self.student_list)

        sys.stdout = sys.__stdout__

        # Compares the right values
        self.assertEqual(output_obj.getvalue(), result)
