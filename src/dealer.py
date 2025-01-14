from src.hand import Hand
import time

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def play_hand(self, deck, max_hand_length):
        """
        This method plays out the dealer's hand using the standard rules.
        Hit until the score is between 17 and 21 or a bust is reached.

        Parameters:
            deck (Deck): the deck object to draw cards from
            max_hand_length (int): the length of the longest hand
        Returns:
            int: the length of the longest hand
        """

        print("=========================================")

        #once all the players have made their decisions, begin the dealer's hand
        print("Play is over. Dealer's turn.")
        time.sleep(1.5)

        #display the dealer's hand while keeping the second card hidden
        print("Dealer: ", end="")
        self.print_hand(max_hand_length)
        time.sleep(1.5)

        #keep track of the length of the hand
        hand_length = 2

        #simulate the dealer's rules until conclusion is reached (a final score between 17 and 21 or a bust)
        while True:
            #display the dealer's hand
            print("Dealer: ", end="")
            super().print_hand(max_hand_length)
            time.sleep(1.5)

            #if a score of 21 or a bust has been reached end the simulation
            if self.score[0] >= 21:
                break
            elif self.score[1] == 21:
                self.stand()
                break
            
            #if the score is too low, draw another card
            if self.score[0] < 17 and self.score[1] < 17:
                #receive an additional card
                card_drawn = deck.draw_card()
                self.hit(card_drawn)

                #increment the current hand length
                hand_length += 1

                #update the maximum hand length
                max_hand_length = max(max_hand_length, hand_length)
            else:
                self.stand()
                break

        print("=========================================")

        return max_hand_length

    def print_hand(self, max_hand_length):
        """
        This method prints the dealer's hand with the second card hidden and not included in the score.

        Parameters:
            max_hand_length (int): the length of the longest hand
        
        Returns:
            None
        """
        #replace the second card with a placeholder
        hidden_cards = self.cards.copy()
        hidden_cards[1] = "??"

        #set the hands score to the value of the first card
        scores = [0, 0]
        if hidden_cards[0][0] != "A":
            scores[0] = Hand.card_value[hidden_cards[0][0]]
        else:
            scores = [1, 11]

        #convert the score of a hand to a string
        score = ""
        if scores[1] == 0:
            score = str(scores[0])
        else:
            score = str(scores[0]) + "/" + str(scores[1])

        print(f"[ {' | '.join(hidden_cards)} ]  " + "     "*(max_hand_length-len(self.cards)) + f"|  {score}")

