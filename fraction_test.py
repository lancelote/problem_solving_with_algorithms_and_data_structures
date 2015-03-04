import unittest
from fraction import Fraction
from fraction import gcd


class GcdTest(unittest.TestCase):

    def gcd_returns_correct_value(self):
        self.assertEqual(gcd(20, 10), 10)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(18, 24), 6)


class FractionTest(unittest.TestCase):

    def setUp(self):
        self.test_fraction = Fraction(1, 2)

    def test_init_works_correct(self):
        self.assertEqual(self.test_fraction.num, 1)
        self.assertEqual(self.test_fraction.den, 2)

    def test_init_raises_typeerror_if_not_int(self):
        self.assertRaises(TypeError, self.test_fraction, "Hello", "World")

    def test_init_raise_valueerror_if_den_is_negative(self):
        self.assertRaises(ValueError, Fraction, 1, -1)

    def test_init_raise_valueerror_if_den_or_num_is_zero(self):
        self.assertRaises(ValueError, Fraction, 0, 1)
        self.assertRaises(ValueError, Fraction, 1, 0)

    def test_str_returns_correct_value(self):
        self.assertEqual(self.test_fraction.__str__(), "1/2")

    def test_add_returns_correct_value(self):
        self.assertEqual((self.test_fraction + Fraction(2, 5)).__str__(), "9/10")