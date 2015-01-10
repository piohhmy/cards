import random

class Card():
    def __init__(self, value, suit=None):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        if self.suit:
            return "{0} of {1}".format(self.value, self.suit)
        else:
            return self.value

class Deck():
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        return self.cards == other.cards

    def __ne__(self, other):
        return not self == other