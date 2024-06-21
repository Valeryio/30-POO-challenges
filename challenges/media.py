#!/usr/bin/env python3

# This module is for the class of the media

from . import Video
from . import Audio

class Media(Audio, Video):
    """This is the media class

    Attributes:
        @name: (str), name of the media
        @category: (str) category of the media
        @duration: (deltatime) duration of the media
    """

    def __init__(self, name, category, duration, artist_name):
        """This is the constructor of the media class"""
        Video.__init__(self, name, duration, category)
        Audio.__init__(self, name, artist_name)
