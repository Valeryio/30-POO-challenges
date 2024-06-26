#!/usr/bin/env python3

# This is the module of the class audio

class Audio():
    """This is the class for audio elements

    Attributes:
        @name: (str) the name of the audio
        @artist_name: (str) the name of the artist
    """

    def __init__(self, name, artist_name):
        """This is the constructor the class

        Args:
            @name: (str), the name of the audio
            @artist_name: (str), the nameof the artist
        """
        
        self.name = name
        self.artist_name = artist_name

    @property
    def name(self):
        """This is the getter of the name"""
        return self.__name

    @property
    def artist_name(self):
        """This is the getter of the artist_name"""
        return self.__artist_name

    @name.setter
    def name(self, name):
        """This is the setter of the name

        Args:
            @name: (str)

        Raises:
            TypeError: if name is not an str
        """

        if type(name) is not str:
            raise TypeError("The name should be a string")
        else:
            self.__name = name

    @artist_name.setter
    def artist_name(self, artist_name):
        """This is the setter of the artist_name

        Args:
            @artist_name: (str)

        Raises:
            TypeError: if artist_name is not an str
        """

        if type(artist_name) is not str:
            raise TypeError("The artist_name should be a string")
        else:
            self.__artist_name = artist_name

    def listen(self):
        print(f"{self.name} audio is playing, artist : {self.artist_name}")

    def stop(self):
        print(f"{self.name} have been stopped!")
