import unittest
from binary_search.binary_search import binary_search, recursion_binary_search


class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5]
        self.test_list_even = [1, 2, 3, 4]

    def test_binary_search_returns_correct_result(self):
        self.assertTrue(binary_search(self.test_list, 1))
        self.assertTrue(binary_search(self.test_list, 2))
        self.assertTrue(binary_search(self.test_list, 3))
        self.assertTrue(binary_search(self.test_list, 4))
        self.assertTrue(binary_search(self.test_list, 5))
        self.assertFalse(binary_search(self.test_list, 0))
        self.assertFalse(binary_search(self.test_list, 6))

        self.assertTrue(binary_search(self.test_list_even, 1))
        self.assertTrue(binary_search(self.test_list_even, 2))
        self.assertTrue(binary_search(self.test_list_even, 3))
        self.assertTrue(binary_search(self.test_list_even, 4))
        self.assertFalse(binary_search(self.test_list_even, 0))
        self.assertFalse(binary_search(self.test_list_even, 5))

        self.assertFalse(binary_search([], 5))


class RecursionBinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5]
        self.test_list_even = [1, 2, 3, 4]

    def test_recursion_binary_search_returns_correct_result(self):
        self.assertTrue(recursion_binary_search(self.test_list, 1))
        self.assertTrue(recursion_binary_search(self.test_list, 2))
        self.assertTrue(recursion_binary_search(self.test_list, 3))
        self.assertTrue(recursion_binary_search(self.test_list, 4))
        self.assertTrue(recursion_binary_search(self.test_list, 5))
        self.assertFalse(recursion_binary_search(self.test_list, 0))
        self.assertFalse(recursion_binary_search(self.test_list, 6))

        self.assertTrue(recursion_binary_search(self.test_list_even, 1))
        self.assertTrue(recursion_binary_search(self.test_list_even, 2))
        self.assertTrue(recursion_binary_search(self.test_list_even, 3))
        self.assertTrue(recursion_binary_search(self.test_list_even, 4))
        self.assertFalse(recursion_binary_search(self.test_list_even, 0))
        self.assertFalse(recursion_binary_search(self.test_list_even, 5))

        self.assertFalse(recursion_binary_search([], 5))