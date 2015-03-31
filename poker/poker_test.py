import unittest
from poker.poker import Card, Pack, Party


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


class PartyTest(unittest.TestCase):

    def setUp(self):
        self.test_party = Party("Name", 100)

    def test_init_raises_valueerror_if_money_0_or_negative(self):
        with self.assertRaises(ValueError):
            Party("Name", 0)
        with self.assertRaises(ValueError):
            Party("Name", -1)

    def test_get_name_returns_correct_result(self):
        self.assertEqual(self.test_party.get_name(), "Name")

    def test_get_wallet_returns_correct_value(self):
        self.assertEqual(self.test_party.get_wallet(), 100)

    def test_change_wallet(self):
        self.test_party.change_wallet(10)
        self.assertEqual(self.test_party.get_wallet(), 110)
        self.test_party.change_wallet(-20)
        self.assertEqual(self.test_party.get_wallet(), 90)
        self.assertRaises(ValueError, self.test_party.change_wallet, -100)
