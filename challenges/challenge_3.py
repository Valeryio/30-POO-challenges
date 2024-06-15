#!/usr/bin/env python3

# This the the module of the class Notes of a student

class Note():
    """
        This is the class relative to notes
    """
    
    def __init__(self, note, student_name):
        """
            This is the constructor of the class

            Args:
                @note (int): the note of the student
                @student_name (string): the name of the student
        """
        self.note = note
        self.student_name = student_name

    @property
    def note(self):
        """This is the getter of the note attribute"""
        return self.__note

    @property
    def student_name(self):
        """This is the getter of the student_name attribute"""
        return self.__student_name

    @note.setter
    def note(self, note):
        """This is the setter of the attribute note"""
        if note < 0:
            self.__note = 0
        else:
            self.__note = note

    @student_name.setter
    def student_name(self, student_name):
        """This is the setter of the attribute student_name"""
        if type(student_name) is not str:
            raise(TypeError("The student name given is not a string"))
            self.__student_name = ""
        else:
            self.__student_name = student_name
