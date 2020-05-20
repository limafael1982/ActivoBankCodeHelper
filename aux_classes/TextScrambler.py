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
        elif char == 'D':
            return 'O'
        elif char == 'e':
            return 'r'
        elif char == 'E':
            return 'R'
        elif char == 'f':
            return 'A'
        elif char == 'F':
            return 'a'
        elif char == 'g':
            return 'x'
        elif char == 'G':
            return 'X'
        elif char == 'h':
            return 'c'
        elif char == 'H':
            return 'C'
        elif char == 'i':
            return 'm'
        elif char == 'I':
            return 'M'
        elif char == 'j':
            return 'u'
        elif char == 'J':
            return 'U'
        elif char == 'k':
            return 'f'
        elif char == 'K':
            return 'F'
        elif char == 'l':
            return 'z'
        elif char == 'L':
            return 'Z'
        elif char == 'm':
            return 'd'
        elif char == 'M':
            return 'D'
        elif char == 'n':
            return 'p'
        elif char == 'N':
            return 'P'
        elif char == 'o':
            return 't'
        elif char == 'O':
            return 'T'
        elif char == 'p':
            return 'v'
        elif char == 'P':
            return 'V'
        elif char == 'q':
            return 'b'
        elif char == 'Q':
            return 'B'
        elif char == 'r':
            return 'g'
        elif char == 'R':
            return 'G'
        elif char == 's':
            return 'h'
        elif char == 'S':
            return 'H'
        elif char == 't':
            return 'k'
        elif char == 'T':
            return 'K'
        elif char == 'u':
            return 'l'
        elif char == 'U':
            return 'L'
        elif char == 'v':
            return 'e'
        elif char == 'V':
            return 'E'
        elif char == 'x':
            return 'J'
        elif char == 'X':
            return 'j'
        elif char == 'z':
            return 'N'
        elif char == 'Z':
            return 'n'
        else:
            return char

    def get_scramble(self):
        word = ''
        for letter in self.input_text:
            sletter = self._change_char(letter)
            word = word + sletter
        return word

