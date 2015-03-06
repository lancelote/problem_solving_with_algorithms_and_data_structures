import unittest
from min_value.min_value import min_value_o_n2, min_value_o_n


class MinValueOn2Test(unittest.TestCase):

    def test_min_value_o_n2_returns_correct_result(self):
        self.assertEqual(min_value_o_n2([3, 2, 1]), 1)
        self.assertEqual(min_value_o_n2([3, 1, 2]), 1)
        self.assertEqual(min_value_o_n2([1, 2, 3]), 1)


class MinValueOnTest(unittest.TestCase):

    def test_min_value_o_n_returns_correct_result(self):
        self.assertEqual(min_value_o_n([3, 2, 1]), 1)
        self.assertEqual(min_value_o_n([3, 1, 2]), 1)
        self.assertEqual(min_value_o_n([1, 2, 3]), 1)