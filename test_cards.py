import unittest

from cards import Card, Deck

class TestCards(unittest.TestCase):
    def test_card_created_with_value(self):
        card = Card('Joker')

        self.assertEqual(card.value, 'Joker')

    def test_card_created_with_value_and_suit(self):
        card = Card('2', 'Spades')

        self.assertEqual(card.value, '2')
        self.assertEqual(card.suit, 'Spades')

    def test_cards_with_same_value_and_suit_are_equal(self):
        card1 = Card('2', 'Spades')
        card2 = Card('2', 'Spades')

        self.assertTrue(card1 == card2)
        self.assertFalse(card1 != card2)

    def test_cards_with_different_values_are_not_equal(self):
        card1 = Card('2', 'Spades')
        card2 = Card('3', 'Spades')

        self.assertTrue(card1 != card2)
        self.assertFalse(card1 == card2)

    def test_card_str_shows_value_and_suit(self):
        card = Card('King', 'Hearts')

        self.assertEqual(str(card), 'King of Hearts')

    def test_card_str_shows_value_only_with_no_suit(self):
        card = Card('King', 'Hearts')

        self.assertEqual(str(card), 'King of Hearts')

class TestDeck(unittest.TestCase):
    def test_deck_with_1_card_has_len_1(self):
        deck = Deck([Card('2', 'Clubs')])

        self.assertEqual(len(deck), 1)
        
    def test_deck_with_52_cards_has_len_52(self):
        cards = [Card('Joker') for _ in range(52)]
        deck = Deck(cards)

        self.assertEqual(len(deck), 52)

    def test_deck_with_same_cards_are_equal(self):
        cards = [Card(str(value), 'Diamonds') for value in range(2,11)]
        deck1 = Deck(cards)
        deck2 = Deck(cards)

        self.assertTrue(deck1 == deck2)
        self.assertFalse(deck1 != deck2)

    def test_deck_with_different_cards_are_not_equal(self):
        cards = [Card(str(value), 'Diamonds') for value in range(2,11)]
        deck1 = Deck(cards)
        deck2 = Deck([Card('Joker')])

        self.assertTrue(deck1 != deck2)
        self.assertFalse(deck1 == deck2)
        

    def test_deck_after_a_shuffle_not_the_same(self):
        cards = [Card(str(value), 'Diamonds') for value in range(2,11)]
        deck1 = Deck(cards)
        deck2 = Deck(list(cards))

        deck1.shuffle()

        self.assertNotEqual(deck1, deck2)

    def test_deck_after_a_shuffle_has_same_len(self):
        cards = [Card('Joker') for _ in range(52)]
        deck = Deck(cards)

        deck.shuffle()

        self.assertEqual(len(deck), 52)

    def test_draw_card_removes_one_card(self):
        cards = [Card('Joker') for _ in range(52)]
        deck = Deck(cards)

        deck.draw()

        self.assertEqual(len(deck), 51)

    def test_draw_card_returns_top_card(self):
        top_card = Card('Ace', 'Clubs')
        cards = [Card('Joker') for _ in range(51)] + [top_card]
        deck = Deck(cards)

        card = deck.draw()

        self.assertEqual(card, top_card)

    def test_draw_card_on_empty_deck_returns_none(self):
        deck = Deck([])

        card = deck.draw()

        self.assertEqual(card, None)

if __name__ == '__main__':
    unittest.main()
