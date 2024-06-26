#!/usr/bin/env python3

# This is the test module for the video class

import sys
import unittest
from io import StringIO
from datetime import timedelta
from challenges.video import Video

class TestVideo (unittest.TestCase):
    """This is the test suite for the video class

    Args:
        @spyder : another video from youtube
        @adore_you : a video from youtube
    """

    def setUp(self):
        """This method sets up all the attributes we'll need through the
        different tests"""
        self.spyder = Video("spyder", "3:09", "video urbaine")
        self.adore_you = Video("adore you", "4:38", "video urbaine")

    def test_attributes(self):
        """This test checks if the different attributes of each object
        have been set correctly"""
        spyder_duration = timedelta(minutes=3, seconds=9)
        adore_you_duration = timedelta(minutes=4, seconds=38)

        self.assertEqual(self.spyder.duration, spyder_duration)
        self.assertEqual(self.adore_you.duration, adore_you_duration)
        self.assertEqual(self.spyder.name, "spyder")
        self.assertEqual(self.adore_you.name, "adore you")
        self.assertEqual(self.spyder.category, "video urbaine")
        self.assertEqual(self.adore_you.category, "video urbaine")

    def output_tester(self, result, test_function):
        """This function checks if an output is what it's supposed to be"""
        output_obj = StringIO()
        sys.stdout = output_obj

        test_function()

        sys.stdout = sys.__stdout__
        self.assertEqual(output_obj.getvalue(), result)

    def test_watch(self):
        """This test checks if the watch() method of the class video works"""
        result = f"spyder video is playing for 0:03:09\n"

        self.output_tester(result, self.spyder.watch)

    def test_stop(self):
        """This test checks if the stop() method of the class video works"""
        result = f"spyder have been stopped!\n"

        self.output_tester(result, self.spyder.stop)
