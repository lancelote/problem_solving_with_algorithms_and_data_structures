import unittest
from anagram.anagram import anagram_1


class AnagramTest(unittest.TestCase):

    def test_anagram_1_returns_correct_result(self):
        self.assertTrue(anagram_1("abcd", "dcba"))
        self.assertFalse(anagram_1("abcde", "abcd"))