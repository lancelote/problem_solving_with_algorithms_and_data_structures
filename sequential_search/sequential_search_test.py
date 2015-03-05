import unittest
from sequential_search.sequential_search import sequential_search, ordered_sequential_search


class SequentialSearchTest(unittest.TestCase):

    def setUp(self):
        self.test_lst = [1, 2, 3]

    def test_sequential_search_returns_correct_result(self):
        self.assertTrue(sequential_search(self.test_lst, 1))
        self.assertFalse(sequential_search(self.test_lst, 4))


class OrderedSequentialSearchTest(unittest.TestCase):

    def setUp(self):
        self.test_lst = [1, 2, 3]

    def test_ordered_sequential_search_returns_correct_result(self):
        self.assertTrue(ordered_sequential_search(self.test_lst, 2))
        self.assertFalse(ordered_sequential_search(self.test_lst, 4))