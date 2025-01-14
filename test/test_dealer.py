import unittest
from unittest.mock import patch
from src.dealer import Dealer
from src.deck import Deck
from src.hand import Hand
import io
import sys


class DealerTestCase(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()

        #capture the printed strings
        captured_output = io.StringIO()
        sys.stdout = captured_output

    def tearDown(self):
        #reset the standard output stream
        sys.stdout = sys.__stdout__

    '''''''''Play hands test'''''''''
    @patch("time.sleep", return_value=None)
    def test_dealer_decision(self, mock_sleep):
        #shuffle the deck
        deck = Deck()
        deck.shuffle()

        hand = Hand()

        for _ in range(1000):
            #reset the dealer's hand
            self.dealer.cards = []
            self.dealer.score = [0, 0]
            self.dealer.state = ""

            #give the dealer a starting hand
            for _ in range(2):
                card_drawn = deck.draw_card()
                self.dealer.hit(card_drawn)

            #simulate the dealer's rules
            self.dealer.play_hand(deck, 2)

            #set up a hand that will walk through the dealers decisions
            hand.cards = []
            hand.score = [0, 0]
            hand.state = ""

            hand.hit(self.dealer.cards[0])
            hand.hit(self.dealer.cards[1])

            #if the dealer should've stood on its starting hand
            if max(hand.score[0], hand.score[1]) >= 17:
                #check that the dealer didnt take another card
                self.assertEqual(len(self.dealer.cards), 2)
            
            #for every card after the starting hand
            for i in range(2, len(self.dealer.cards)):
                hand.hit(self.dealer.cards[i])

                score = max(hand.score[0], hand.score[1])

                #if the score is one that should be stood on
                if score >= 17:
                    #check that the dealer didnt take another card
                    self.assertEqual(len(self.dealer.cards), i+1)
                else:
                    #if the dealer shouldve hit then check that the next card exists
                    try:
                        self.dealer.cards[i+1]
                    except:
                        self.fail("Dealer did not hit when they were supposed to")

if __name__ == '__main__':
    unittest.main()
