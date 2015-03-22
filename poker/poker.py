# ♠, ♥, ♦, ♣


class Card():

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
