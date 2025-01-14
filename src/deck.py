import random

class Deck:
    """
    Represents a standard deck of 52 playing cards. 
    The deck contains cards with values from 2 to Ace and 4 suits: Clubs (♣), Diamonds (♦), Hearts (♥), and Spades (♠).
    
    Attributes:
        cards (list): A list containing all the cards in the deck, represented as strings 
                      combining the value and suit.
        card_pos (int): The current position in the deck, used for drawing cards sequentially.
        cut (int): The index of where the cut card is placed, a random point between
                   60% and 75% of the deck's length.
    """

    def __init__(self):
        self.cards = []
        self.card_pos = 0
        self.cut = 0

        values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suits = ["♣", "♦", "♥", "♠"]

        #for every combination of card value and suit
        for suit in suits:
            for value in values:
                self.cards.append(value+suit)
    
    def shuffle(self):
        """
        Shuffle the deck randomly and set up the cut card between 60% and 75% through the deck.
        The cut card is present to prevent effective card counting.

        Parameters:
            None
        
        Returns:
            None
        """

        #shuffle the deck
        random.shuffle(self.cards)
        
        #initialise cut card and reset the current card position
        self.cut = random.randint(int(52*0.60), int(52*0.75))
        self.card_pos = 0

    def draw_card(self):
        """
        This method returns the next card in the deck and updates the current card position.
        If the cut card has been reached then the deck is reshuffled before a card is drawn.

        Parameters:
            None
        
        Returns:
            str: the next card in the deck
        """

        #if the cut card has been reached
        if self.card_pos >= self.cut:
            print("Deck was reshuffled!")

            #reshuffle
            self.shuffle()
        
        #increment the current card position
        self.card_pos += 1

        #return the next card in the deck
        return self.cards[self.card_pos-1]
