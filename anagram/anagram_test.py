import unittest
from anagram.anagram import anagram_1, anagram_2


class AnagramTest(unittest.TestCase):

    def test_anagram_1_returns_correct_result(self):
        self.assertTrue(anagram_1("abcd", "dcba"))
        self.assertFalse(anagram_1("abcde", "dcbaf"))

    def test_anagram_2_returns_correct_result(self):
        self.assertTrue(anagram_2("abcd", "dcba"))
        self.assertFalse(anagram_2("abcde", "dcbaf"))