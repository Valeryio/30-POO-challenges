#!/usr/bin/env python3

# This is the module for the video class

from datetime import timedelta

class Video():
    """This is the class for videos

    Attributes:
        @name: (str) name of the video
        @duration: (timedelta) duration of the video
        @category: (str) category of the video
    """

    def __init__(self, name, duration, category):
        """This is the constructor of the class

        Arguments:
            @name: (str)
            @duration: (string)
            @category: (string)
        """
        self.name = name
        self.duration = duration
        self.category = category

    @property
    def name(self):
        """This is the getter of the attribute name"""
        return self.__name

    @property
    def duration(self):
        """This is the getter of the attribute duration"""
        return self.__duration

    @property
    def category(self):
        """This is the getter of the attribute duration"""
        return self.__category

    @name.setter
    def name(self, name):
        """This is the setter of the attribute name"""
        if type(name) is not str:
            raise TypeError("The name attribute should be str")
        else:
            self.__name = name

    @duration.setter
    def duration(self, duration):
        """This is the setter of the attribute duration"""

        self.__duration = self.parse_duration(duration)


    @category.setter
    def category(self, category):
        """This is the setter of the attribute category"""
        if type(category) is not str:
            raise TypeError("The category attribute should be str")
        else:
            self.__category = category

    def parse_duration(self, duration_string):
        """This method parse the duration from string to timedelta object"""
        time_infos = duration_string.split(':')
        time_infos = list(map(int, time_infos))

        if len(time_infos) == 3:
            return timedelta(hours=time_infos[0], minutes=time_infos[1], \
                    seconds=time_infos[2])
        elif len(time_infos) == 2:
            return timedelta(minutes = time_infos[0], seconds=time_infos[1])
        elif len(time_infos) == 1:
            return timedelta(seconds=time_infos[0])

    def watch(self):
        """This method watch the video"""
        print(f"{self.name} video is playing for {self.duration}")

    def stop(self):
        """This method stop the watching of a video"""
        print(f"{self.name} have been stopped!")
