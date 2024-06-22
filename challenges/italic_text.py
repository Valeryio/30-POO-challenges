#!/usr/bin/env python3

# This is the module of the class ItalicText

from . import Text

class ItalicText(Text):
    """This class is a customised class for strings
    Attributes:
        @sentence: (str), the string to customise
    """

    def __init__(self, sentence):
        """This is the constructor of the class"""
        super().__init__(sentence)

    def show_text(self):
        """This method prints the sentence"""
        print('_' + self.sentence + '_')
