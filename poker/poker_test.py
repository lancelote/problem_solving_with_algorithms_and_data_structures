import unittest
from poker.poker import Card, Pack


class CardTest(unittest.TestCase):

    def setUp(self):
        self.test_card = Card(2, "hearts")

    def test_init_raises_error_if_wrong_suit(self):
        with self.assertRaises(ValueError):
            Card(2, "Hello")

    def test_init_raises_error_if_wrong_value(self):
        with self.assertRaises(ValueError):
            Card(1, "hearts")

    def test_get_value_returns_correct_result(self):
        self.assertEqual(self.test_card.get_value(), 2)

    def test_get_suit_returns_correct_result(self):
        self.assertEqual(self.test_card.get_suit(), "hearts")


class PackTest(unittest.TestCase):

    def setUp(self):
        self.pack = Pack()
        self.ideal_pack = [(value, suit)
                           for value in range(2, 15)
                           for suit in ("spades", "hearts", "diamonds", "clubs")]

    def test_cards_method_returns_correct_result(self):
        self.assertListEqual(self.pack.cards(), self.ideal_pack)
