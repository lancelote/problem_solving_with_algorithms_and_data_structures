import unittest
from insertion_sort.insertion_sort import insertion_sort


class SelectionSortTest(unittest.TestCase):

    def test_insertion_sort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        insertion_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        insertion_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])