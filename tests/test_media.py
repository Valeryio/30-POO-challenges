#!/usr/bin/env python3

# This is the test module for the media class

import unittest
from datetime import timedelta
from challenges.media import Media

class TestMedia(unittest.TestCase):
    """This is the suite test for the media class

    Args:
        @spyder : (media object)
        @ftnd : (media object)
    """

    def setUp(self):
        """This method sets up all the objetcs used for the different tests"""
        self.spyder = Media("spyder", "music", "3:09", "GIMS")
        self.assez = Media("Assez", "music", "03:26", "Dadju")

    def test_attributes(self):
        """This test checks if all the attributes of the media have been set"""
        spyder_duration = timedelta(minutes=3, seconds=9)
        assez_duration = timedelta(minutes=3, seconds=26)

        self.assertEqual(self.spyder.duration, spyder_duration)
        self.assertEqual(self.assez.duration, assez_duration)
        self.assertEqual(self.assez.name, "Assez")
        self.assertEqual(self.assez.category, "music")
        self.assertEqual(self.assez.artist_name, "Dadju")
