# -*- coding: utf-8 -*-


class TextUnscrambler:
    """
    This class is responsible for text unscrambling.
    """

    def __init__(self, input_text):
        self.input_text = input_text

    def _change_char(self, char):
        if char == 'i':
            return 'a'
        elif char == 'I':
            return 'A'
        elif char == 's':
            return 'b'
        elif char == 'S':
            return 'B'
        elif char == 'q':
            return 'c'
        elif char == 'Q':
            return 'C'
        elif char == 'o':
            return 'd'
        elif char == 'O':
            return 'D'
        elif char == 'r':
            return 'e'
        elif char == 'R':
            return 'E'
        elif char == 'A':
            return 'f'
        elif char == 'a':
            return 'F'
        elif char == 'x':
            return 'g'
        elif char == 'X':
            return 'G'
        elif char == 'c':
            return 'h'
        elif char == 'C':
            return 'H'
        elif char == 'm':
            return 'i'
        elif char == 'M':
            return 'I'
        elif char == 'u':
            return 'j'
        elif char == 'U':
            return 'J'
        elif char == 'f':
            return 'k'
        elif char == 'F':
            return 'K'
        elif char == 'z':
            return 'l'
        elif char == 'Z':
            return 'L'
        elif char == 'd':
            return 'm'
        elif char == 'D':
            return 'M'
        elif char == 'p':
            return 'n'
        elif char == 'P':
            return 'N'
        elif char == 't':
            return 'o'
        elif char == 'T':
            return 'O'
        elif char == 'v':
            return 'p'
        elif char == 'V':
            return 'P'
        elif char == 'b':
            return 'q'
        elif char == 'B':
            return 'Q'
        elif char == 'g':
            return 'r'
        elif char == 'G':
            return 'R'
        elif char == 'h':
            return 's'
        elif char == 'H':
            return 'S'
        elif char == 'k':
            return 't'
        elif char == 'K':
            return 'T'
        elif char == 'l':
            return 'u'
        elif char == 'L':
            return 'U'
        elif char == 'e':
            return 'v'
        elif char == 'E':
            return 'V'
        elif char == 'J':
            return 'x'
        elif char == 'j':
            return 'X'
        elif char == 'N':
            return 'z'
        elif char == 'n':
            return 'Z'
        else:
            return char

    def get_unscramble(self):
        word = ''
        for letter in self.input_text:
            sletter = self._change_char(letter)
            word = word + sletter
        return word

