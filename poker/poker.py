# ♠, ♥, ♦, ♣


class Card:

    def __init__(self, value, suit):
        if value not in range(2, 15):
            raise ValueError("Unknown value!")
        else:
            self.value = value

        if suit not in ("spades", "hearts", "diamonds", "clubs"):
            raise ValueError("Unknown suit!")
        else:
            self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class Pack:
    """
    Pack of cards: 15 cards by 4 suits
    """

    def __init__(self):
        self.cards_list = [(value, suit)
                           for value in range(2, 15)
                           for suit in ("spades", "hearts", "diamonds", "clubs")]

    def cards(self):
        return self.cards_list


class Party:
    """
    General class represents a party in the game: player, bot and table
    """

    def __init__(self, name, money):
        self.name = name
        if money <= 0:
            raise ValueError("Party wallet cannot be 0 or negative")
        else:
            self.wallet = money

    def get_name(self):
        return self.name

    def get_wallet(self):
        return self.wallet

    def change_wallet(self, change):
        if change + self.wallet < 0:
            raise ValueError("Wallet cannot be negative")
        else:
            self.wallet += change