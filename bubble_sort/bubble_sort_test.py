import unittest
from bubble_sort.bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_bubble_sort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        bubble_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        bubble_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])