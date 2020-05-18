# -*- coding: utf-8 -*-


class TextScrambler:
    """
    This class is responsible for text scrambling.
    Note that scrambling is not encrypting.
    """

    def __init__(self, input_text):
        self.input_text = input_text

    def _change_char(self, char):
        if char == 'a':
            return 'i'
        elif char == 'A':
            return 'I'
        elif char == 'b':
            return 's'
        elif char == 'B':
            return 'S'
        elif char == 'c':
            return 'q'
        elif char == 'C':
            return 'Q'
        elif char == 'd':
            return 'o'

        else:
            return char

    def scramble(self):
        word = ''
        for letter in self.input_text:
            sletter = self._change_char(letter)
            word = word + sletter
        return word

