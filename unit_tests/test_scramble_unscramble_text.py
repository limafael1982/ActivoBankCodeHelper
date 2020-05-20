# -*- coding: utf-8 -*-

import unittest
from aux_classes.TextScrambler import TextScrambler
from aux_classes.TextUnsrambler import TextUnscrambler


class TestTextScrambleAndUnscrambler(unittest.TestCase):

    def test_should_scramble_and_unscramble_correctly(self):
        text = 'abcdefghijklmnopqrstuwxyz ABCDEFGHIJKLMNOPQRSTUWXYZ'
        text_scrambler_obj = TextScrambler(text)
        scrambled_text = text_scrambler_obj.get_scramble()
        text_unscrabmler_obj = TextUnscrambler(scrambled_text)
        self.assertEqual(text, text_unscrabmler_obj.get_unscramble())

