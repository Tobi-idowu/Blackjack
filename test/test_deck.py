import unittest
from src.deck import Deck
import io
import sys

class DeckTestCase(unittest.TestCase):

    # i chose to shuffle the deck in the set up function because the 
    # deck is only intended for use after it has been shuffled
    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()

        #capture the printed strings
        captured_output = io.StringIO()
        sys.stdout = captured_output

    def tearDown(self):
        #reset the standard output stream
        sys.stdout = sys.__stdout__

    '''''''''Deck of cards tests'''''''''
    def test_number_of_cards(self):
        #check if the number of cards in the deck is 52
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    def test_uniqueness(self):
        #check if all the cards in the deck are unique
        set_of_cards = set(self.deck.cards)
        self.assertEqual(len(set_of_cards), 52)
    
    def test_number_of_occurrences_ranks(self):
        count = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, 
                 "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}
        
        #count the occurrences the of each card rank
        for card in self.deck.cards:
            value = card[0]
            count[value] += 1

        #assert the count of each rank to be 4
        for rank in count:
            self.assertEqual(count[rank], 4)

    def test_number_of_occurrences_suits(self):
        count = {"♣": 0, "♦": 0, "♥": 0, "♠": 0}

        #count the occurrences of each suit
        for card in self.deck.cards:
            value = card[1]
            count[value] += 1

        #assert the count of each suit to be 13
        for rank in count:
            self.assertEqual(count[rank], 13)

    def test_card_position(self):
        self.assertEqual(self.deck.card_pos, 0)

    def test_cut_card_position(self):
        #check if the cut card's position is valid
        assert int(52*0.60) <= self.deck.cut <= int(52*0.75)

    '''''''''Draw cards tests'''''''''
    def test_update_card_position(self):
        #check if the card position is updated correctly when a card is drawn
        for i in range(self.deck.cut):
            self.assertEqual(self.deck.card_pos, i)
            self.deck.draw_card()

    def test_draw_card_past_cut_card(self):
        for _ in range(self.deck.cut):
            self.deck.draw_card()

        #check if drawing a card past the cut card results in a reset of the card position
        self.deck.draw_card()

        self.assertEqual(self.deck.card_pos, 1)

    def test_drawn_card(self):
        #check if the draw_card() returns the correct card
        for i in range(self.deck.cut):
            self.assertEqual(self.deck.draw_card(), self.deck.cards[i])


if __name__ == '__main__':
    unittest.main()
