import unittest
from shell_sort.shell_sort import shell_sort


class ShellSortTest(unittest.TestCase):

    def test_shell_cort_works_correct(self):
        lst = [5, 4, 3, 2, 1]
        shell_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])
        lst = [1, 3, 2, 5, 4]
        shell_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])