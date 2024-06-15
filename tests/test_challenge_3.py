#!/usr/bin/env python3

"""
    This is the test module of the class ...
"""

import sys
import unittest
from io import StringIO
from challenges.challenge_3 import Note


class TestNote(unittest.TestCase):
    """ This is the testclass for the Note Class"""

    def setUp(self):
        """This methods define all the attributes  needed in the test class"""
        self.math_note = Note(16, "Jul")
        self.french_note = Note(4, "Max")

    def test_attributes(self):
        """This class test the attrributes of the class"""
        self.assertEqual(self.math_note.note, 16)
        self.assertEqual(self.math_note.student_name, "Jul")

        with self.assertRaises(TypeError):
            pct_note = Note(-14, -56)

            self.assertEqual(pct_note.note, 0)
            self.assertEqual(pct_note.student_name, "")

    def test_have_succeded(self):
        """This method test the property have_succeded of the Note class"""
        success_result = f"{self.math_note.student_name} have succeeded! Congrats!\n"
        fail_result = f"{self.french_note.student_name} have not succeeded! Sorry!\n"

        # Create two distinct stringIO object to get the right and the wrong output
        output_obj = StringIO()
        fail_output_obj = StringIO()

        # Verify the right output
        sys.stdout = output_obj
        self.math_note.success()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_obj.getvalue(), success_result)

        # Verify the wrong output
        sys.stdout = fail_output_obj
        self.french_note.success()
        sys.stdout = sys.__stdout__
        self.assertEqual(fail_output_obj.getvalue(), fail_result)
