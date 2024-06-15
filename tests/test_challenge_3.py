#!/usr/bin/env python3

"""
    This is the test module of the class ...
"""

import unittest
from challenges.challenge_3 import Note


class TestNote(unittest.TestCase):
    """ This is the testclass for the Note Class"""

    def setUp(self):
        """This methods define all the attributes  needed in the test class"""
        self.math_note = Note(16, "Jul")
#        self.pct_note = Note(-14, -56)

    def test_attributes(self):
        """This class test the attrributes of the class"""
        self.assertEqual(self.math_note.note, 16)
        self.assertEqual(self.math_note.student_name, "Jul")

        with self.assertRaises(TypeError):
            pct_note = Note(-14, -56)

            self.assertEqual(pct_note.note, 0)
            self.assertEqual(pct_note.student_name, "")
