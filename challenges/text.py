#!/usr/bin/env python3

# This is the module of the class Text

class Text():
    """This class is a customised class for strings
    Attributes:
        @sentence: (str), the string to customise
    """

    def __init__(self, sentence):
        """This is the constructor of the class"""
        self.sentence = sentence
    
    @property
    def sentence(self):
        """This is the getter for the attribute sentence"""
        return self.__sentence

    @sentence.setter
    def sentence(self, sentence):
        if type(sentence) is str:
            self.__sentence = sentence
        else:
            raise TypeError()

    def show_text(self):
        print(self.sentence)
