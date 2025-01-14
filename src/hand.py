class Hand:
    """
    Represents a hand of cards in a blackjack game.

    This class keeps track of the cards in the hand and the total value of the hand.

    Attributes:
        cards (list): a list of cards in the hand where each card is represented as a string
        value (list): a list of length 2 that represents the value of the hand
               - value[0] is the total value if Aces are treated as 1
               - value[1] is the total value if Aces are treated as 11 or is kept at 0 if there is no Ace
        state (str): a record of the state of the hand (win, loss, push, bust)
        card_value (dict): a dictionary mapping each card to its corresponding numeric value
                    - it is a class variable shared by all instances
                    - For Aces, the value is 1 (with special handling for Ace being 11)
    """

    #using a dictionary for value lookups is faster than checking if card is a face card or converting to an integer 
    card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9, "T": 10, "J": 10, "Q":10, "K": 10, "A": 1}

    def __init__(self):
        #list of the cards in the hand
        self.cards = []
        self.score = [0, 0]
        self.state = ""
    
    def hit(self, card):
        """
        Adds a new card to the hand and updates the hand's value.
        If the card is an Ace, it may be treated as 1 or 11 depending on the hand's total value.
        If the hand exceeds a total value of 21, it is considered a bust.
        
        Parameters:
            card (str): The card to be added to the hand
        
        Returns:
            None
        """

        #add the card to the hand
        self.cards.append(card)

        #remove the suit of the card
        card = card[0]

        #add the value of the card to the hand
        self.score[0] += Hand.card_value[card]

        #if the hand has bust
        if self.score[0] > 21:
            self.state = "BUST"
            return

        #if the hand doesn't have an ace
        if self.score[1] != 0:
            self.score[1] += Hand.card_value[card]

            if self.score[1] > 21:
                self.score[1] = 0

        #if the hit card is an Ace and it is the first one in the hand, then its value can be both a 1 or an 11
        elif card == "A" and self.score[0] <= 11:
            self.score[1] = self.score[0] + 10        #treat Ace as 11

    
    def stand(self):
        """
        This method consolidates a hands score by collapsing two scores into one.
        
        Parameters:
            None
        
        Returns:
            None
        """

        #if the player's hand has two values pick the highest one
        if self.score[1] != 0:
            self.score[0] = self.score[1]
            self.score[1] = 0

    def evaluate(self, dealer_score):
        """
        This method classifies a hand as a win, loss or push depending on the dealers score

        Parameter:
            dealer_score (int): the score that the dealer reached or -1 if they bust
        Returns:
            None
        """

        #if the hand hasn't bust already
        if self.state == "":
            if self.score[0] > dealer_score:
                self.state = "WIN"
            elif self.score[0] < dealer_score:
                self.state = "LOSS"
            else:
                self.state = "PUSH"

    
    def print_hand(self, max_hand_length, eval = False):
        """
        This method displays the details of a hand. 

        If eval is true then it will display the result of the hand in terms of a win, loss, push or bust.
        If hidden is true, the second card in the hand is hidden and not accounted for in the score, 
        this setting is used for the dealer's hand before all the players have finalised their decisions.

        Parameters:
            max_hand_length (int): the number of cards in the longest hand
                                   - this is used for visual presentation purposes
            hidden (bool): whether the second card in the hand is hidden or not
            eval (bool): whether the hand has been evaluated yet
        
        Returns:
            None
        """

        #if the hand has been evaluated as a win, loss, push or bust
        if eval == True:
            print(f"[ {' | '.join(self.cards)} ]  " + "     "*(max_hand_length-len(self.cards)) + f"|  {self.state} ({self.score[0]})")
            return
        
        score = ""

        #if the hand has one score
        if self.score[1] == 0:
            #if the hand has bust
            if self.score[0] > 21:
                score = "BUST (" + str(self.score[0]) + ")"
            else:
                score = str(self.score[0])
        else:
            #combine the two scores of the hand into one string
            score = str(self.score[0]) + "/" + str(self.score[1])

        print(f"[ {' | '.join(self.cards)} ]  " + "     "*(max_hand_length-len(self.cards)) + f"|  {score}")
