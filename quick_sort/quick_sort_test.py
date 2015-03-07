import unittest
from quick_sort.quick_sort import quick_sort


class QuickSortTest(unittest.TestCase):

    def test_quick_sort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        quick_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        quick_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])