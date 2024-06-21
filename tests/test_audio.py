#!/usr/bin/env python3

# This is the test module for the audio class

import sys
import unittest
from io import StringIO
from challenges.audio import Audio

class TestAudio (unittest.TestCase):
    """This is the test suite for the video class

    Args:
        @spyder : another video from youtube
        @adore_you : a video from youtube
    """

    def setUp(self):
        """This method sets up all the attributes we'll need through the
        different tests"""
        self.spyder = Audio("spyder", "GIMS")
        self.adore_you = Audio("adore you", "Myley Cirus")

    def test_attributes(self):
        """This test checks if the different attributes of each object
        have been set correctly"""
        self.assertEqual(self.spyder.name, "spyder")
        self.assertEqual(self.adore_you.name, "adore you")
        self.assertEqual(self.spyder.artist_name, "GIMS")
        self.assertEqual(self.adore_you.artist_name, "Myley Cirus")

    def output_tester(self, result, test_function):
        """This function checks if an output is what it's supposed to be"""
        output_obj = StringIO()
        sys.stdout = output_obj

        test_function()

        sys.stdout = sys.__stdout__
        print(output_obj.getvalue())
        self.assertEqual(output_obj.getvalue(), result)

    def test_listen(self):
        """This test checks if the watch() method of the class audio works"""
        result = f"spyder audio is playing, artist : GIMS\n"

        self.output_tester(result, self.spyder.listen)

    def test_stop(self):
        """This test checks if the stop() method of the class audio works"""
        result = f"spyder have been stopped!\n"

        self.output_tester(result, self.spyder.stop)
