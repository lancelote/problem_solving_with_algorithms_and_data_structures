import unittest
from fraction import Fraction
from fraction import gcd


class GcdTest(unittest.TestCase):

    def gcd_returns_correct_result(self):
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

    def test_str_returns_correct_result(self):
        self.assertEqual(self.test_fraction.__str__(), "1/2")

    def test_add_returns_correct_result(self):
        self.assertEqual(Fraction(1, 2) + Fraction(2, 5), Fraction(9, 10))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 4), Fraction(3, 4))
        self.assertEqual(Fraction(1, 2) + 0, Fraction(1, 2))

    def test_eq_returns_correct_result(self):
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))
        self.assertFalse(Fraction(1, 2) == 0)

    def test_sub_returns_correct_result(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), 0)
        self.assertEqual(Fraction(1, 4) - Fraction(1, 2), Fraction(-1, 4))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 4), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) - 0, Fraction(1, 2))

    def test_mul_returns_correct_result(self):
        self.assertEqual(Fraction(1, 2)*Fraction(3, 4), Fraction(3, 8))
        self.assertEqual(Fraction(3, 4)*Fraction(4, 6), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2)*0, 0)

    def test_truediv_returns_correct_result(self):
        self.assertEqual(Fraction(1, 2)/Fraction(3, 4), Fraction(2, 3))

    def test_truediv_raises_zerodivisionerror(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2)/0

    def test_lt_returns_correct_result(self):
        self.assertTrue(Fraction(1, 4) < Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) < Fraction(1, 4))
        self.assertTrue(Fraction(-1, 2) < 0)
        self.assertFalse(Fraction(1, 2) < 0)

    def test_gt_returns_correct_result(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 4))
        self.assertFalse(Fraction(1, 4) > Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) > 0)
        self.assertFalse(Fraction(-1, 2) > 0)