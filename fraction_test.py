import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):

    def setUp(self):
        self.test_fraction = Fraction(1, 2)

    def test_init(self):
        self.assertEqual(self.test_fraction.num, 1)
        self.assertEqual(self.test_fraction.den, 2)
        self.assertRaises(TypeError, self.test_fraction, "Hello", "World")

    def test_str(self):
        self.assertEqual(self.test_fraction.__str__, "1/2")