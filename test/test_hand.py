import unittest
from src.hand import Hand
from src.deck import Deck


class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def tearDown(self):
        pass

    '''''''''Hit tests'''''''''
    def test_hit_adds_card_to_list(self): 
        deck = Deck()
        deck.shuffle()

        #check if the hit card is appended to the cards list
        for i in range(deck.cut):
            card_drawn = deck.draw_card()
            self.hand.hit(card_drawn)

            self.assertEqual(self.hand.cards, deck.cards[:i+1])

    def test_hit_update_score_one_card(self):
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        
        #check if the a score of a hand is updated correct (one card only)
        for card in cards:
            #reset the hand
            self.hand.cards = []
            self.hand.score = [0, 0]
            self.hand.state = ""

            #add card to hand
            self.hand.hit(card + "♣")
            
            #calculate score[0]
            total = Hand.card_value[card]

            if card == "A":
                self.assertEqual(self.hand.score, [1, 11])
            else:
                self.assertEqual(self.hand.score, [total, 0])

    def test_hit_update_score_two_cards(self):
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

        #check if the a score of a hand is updated correct (two cards only)
        for card1 in cards:
            for card2 in cards:
                #reset the hand
                self.hand.cards = []
                self.hand.score = [0, 0]
                self.hand.state = ""
    
                #add cards to the hand
                self.hand.hit(card1 + "♣")
                self.hand.hit(card2 + "♣")

                #calculate score[0]
                total = Hand.card_value[card1] + Hand.card_value[card2]

                #if an ace is in the hand then assign score[1] accordingly
                if "A" in [card1, card2] and total < 12:
                    self.assertEqual(self.hand.score, [total, total + 10])
                else:
                    self.assertEqual(self.hand.score, [total, 0])

    def test_hit_update_score_three_cards(self):
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        
        #check if the a score of a hand is updated correct (three cards only)
        for card1 in cards:
            for card2 in cards:
                for card3 in cards:
                    #reset the hand
                    self.hand.cards = []
                    self.hand.score = [0, 0]
                    self.hand.state = ""
        
                    #add the cards to the hand
                    self.hand.hit(card1 + "♣")
                    self.hand.hit(card2 + "♣")
                    self.hand.hit(card3 + "♣")

                    #calculate score[0]
                    total = Hand.card_value[card1] + Hand.card_value[card2] + Hand.card_value[card3]

                    #if an ace is in the hand then assign score[1] accordingly
                    if "A" in [card1, card2, card3] and total < 12:
                        self.assertEqual(self.hand.score, [total, total + 10])
                    else:
                        self.assertEqual(self.hand.score, [total, 0])

    def test_hit_state(self):
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        
        for card1 in cards:
            for card2 in cards:
                for card3 in cards:
                    #resst hand
                    self.hand.cards = []
                    self.hand.score = [0, 0]
                    self.hand.state = ""
        
                    #add cards to the hand
                    self.hand.hit(card1 + "♣")
                    self.hand.hit(card2 + "♣")
                    self.hand.hit(card3 + "♣")

                    #calculate score[0]
                    total = Hand.card_value[card1] + Hand.card_value[card2] + Hand.card_value[card3]

                    #check the state of the hand
                    if total > 21:
                        self.assertEqual(self.hand.state, "BUST")
                    else:
                        self.assertEqual(self.hand.state, "")


    '''''''''Stand tests'''''''''
    def test_stand_1_score(self): 
        for i in range(1, 22):
            self.hand.score = [i, 0]
        
            self.hand.stand()

            #check if the stand() method consolidates the score correctly
            self.assertEqual(self.hand.score, [i, 0])
    
    def test_stand_2_scores(self): 
        for i in range(1, 12):
            self.hand.score = [i, i+10]
        
            self.hand.stand()

            #check if the stand() method consolidates the score correctly
            self.assertEqual(self.hand.score, [i+10, 0])

    '''''''''Evaluate tests'''''''''
    def test_evaluate_win(self):
        for i in range(2, 22):
            #for each dealer score that loses to the player
            for j in range(-1, i):
                self.hand.score = [i, 0]

                self.hand.evaluate(j)

                #check if the state was set to a win
                self.assertEqual(self.hand.state, "WIN")

    def test_evaluate_loss(self):
        for i in range(2, 22):
            #for each dealer score that beats the player
            for j in range(i+1, 22):
                self.hand.score = [i, 0]

                self.hand.evaluate(j)

                #check if the state was set to a loss
                self.assertEqual(self.hand.state, "LOSS")

    def test_evaluate_push(self):
        for i in range(2, 22):
            #the dealer and player scores are made to be equal
            self.hand.score = [i, 0]

            self.hand.evaluate(i)

            #check if the state is set to push
            self.assertEqual(self.hand.state, "PUSH")
    
    def test_evaluate_bust(self):
        for i in range(-1, 22):
            self.hand.state = "BUST"

            self.hand.evaluate(i)

            #make sure the state isn't changed when the hand has already bust
            self.assertEqual(self.hand.state, "BUST")


if __name__ == '__main__':
    unittest.main()
