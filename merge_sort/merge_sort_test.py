import unittest
from merge_sort.merge_sort import merge_sort


class MergeSortTest(unittest.TestCase):

    def test_merge_sort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        merge_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        merge_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])