import unittest
from selection_sort.selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_selection_sort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        selection_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        selection_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])