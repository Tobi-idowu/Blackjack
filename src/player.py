from src.hand import Hand
import time

class Player():
    def __init__(self, num_hands):
        self.hands = [Hand() for _ in range(num_hands)]
    
    def play_hands(self, i, players, dealer, deck, max_hand_length):
        """
        This method allows a player to play out all of their hands.

        Parameters:
            i (int): the index of the current player
            players (List[Player]): list of all players in the game
            dealer (Dealer): the dealer's hand
            deck (Deck): the deck object to draw cards from
            max_hand_length (int): the length of the longest hand
        Returns:
            int: the length of the longest hand
        """

        length = len(self.hands)
        j = 0

        while j < length:
            #placeholder for the current hand
            hand = self.hands[j]

            #keep track of the number of cards in the hand to possible update max_hand_length
            hand_length = len(hand.cards)

            #while the current hand is still in play
            while True:
                #if the hand has bust or reached 21 then it is over
                if hand.score[0] > 21:
                    print("Too many (" + str(hand.score[0]) + ")")
                    time.sleep(2)
                    break
                elif hand.score[0] == 21:
                    print("You reached 21")
                    time.sleep(2)
                    break
                elif hand.score[1] == 21:
                    #if a perfect 21 was reached, display the state of the game
                    if hand_length == 2:
                        print_state(players, dealer, max_hand_length)
                        print(f"Player {i+1} Hand {j+1}: ", end="")
                    
                    hand.stand()

                    print("You reached 21")
                    time.sleep(2)

                    break
                
                #display the state of the game
                print_state(players, dealer, max_hand_length)

                print(f"Player {i+1} Hand {j+1}: ", end="")

                #get user input from the player, they will decide to stand, hit or split if possible
                if len(hand.cards) == 2 and hand.cards[0][0] == hand.cards[1][0]:
                    action = get_user_action(hand, dealer, True)
                else:
                    action = get_user_action(hand, dealer)

                if action == "stand":
                    hand.stand()
                    break
                elif action == "hit":
                    #add another card to the hand
                    card_drawn = deck.draw_card()
                    hand.hit(card_drawn)

                    #increment the current hand length
                    hand_length += 1

                    #update the maximum hand length
                    max_hand_length = max(max_hand_length, hand_length)
                elif action == "split":
                    self.split(j)

                    #set up the next iteration
                    hand = self.hands[j]
                    hand_length = 1
                    length += 1


            j += 1

        return max_hand_length
    
    def split(self, j):
        '''
        This method splits hand[j] into two hands and inserts the second hand into position j+1.

        Parameters:
            j (int): the index of the hand that is to be split
        Returns:
            None
        '''
        
        #save the old hand
        hand = self.hands[j]

        #split the two cards into two different hands
        self.hands[j] = Hand()
        self.hands[j].hit(hand.cards[0])

        self.hands.insert(j+1, Hand())
        self.hands[j+1].hit(hand.cards[1])


def get_user_action(hand, dealer, split = False):
    """
    Prompt the user to decide whether to 'stand' or 'hit' based on their hand and the dealer's visible card.
    
    Paarameters:
        hand (Hand): the player's hand object containing their cards and scores
        dealer (Dealer): the dealer's hand object containing their cards and scores

    Returns:
        str: The player's chosen action
    """

    player_score = ""
    dealer_score = ""

    #assign the player a score
    if hand.score[1] == 0:
        player_score = str(hand.score[0])
    else:
        player_score = str(hand.score[0]) + "/" + str(hand.score[1])

    #assign the dealer a score based on their first card
    if dealer.cards[0][0] != "A":
        dealer_score = str(Hand.card_value[dealer.cards[0][0]])
    else:
        dealer_score = "1/11"
            
    while True:
        #get user input
        if split == False:
            action = input(f"You have {player_score} against a dealer's {dealer_score}. Would you like to stand or hit?: ").strip().lower()
                
            #input validation
            if action not in ["stand", "hit"]:
                print("Please choose between stand or hit.")
            else:
                return action
        else:
            action = input(f"You have {player_score} against a dealer's {dealer_score}. Would you like to stand, hit or split?: ").strip().lower()
                
            #input validation
            if action not in ["stand", "hit", "split"]:
                print("Please choose between stand, hit or split.")
            else:
                return action
        
        
def print_state(players, dealer, max_hand_length, eval = False):
    """
    This method displays the current state of the game.

    Parameters:
        players (List[Player]): list of all players in the game
        dealer (Dealer): the dealer's hand
        max_hand_length (int): the length of the longest hand
                               -it is used to make the format of the display consistent
        hidden (bool): signifies whether the dealer's second card should be hidden or not
        eval (bool): signifies whether the final result of each hand should be displayed

    Returns:
        None
    """

    print("\n=========================================")
    
    #display dealer's hand, may or may not hide the second card
    print(f"Dealer: ", end="")

    if eval == True:
        Hand.print_hand(dealer, max_hand_length)
    else:
        dealer.print_hand(max_hand_length)
    print()

    #display each hand for each player
    for i in range(len(players)):
        print(f"Player {i+1}:")

        for j in range(len(players[i].hands)):
            print(f"Hand {j+1}: ", end="")
            players[i].hands[j].print_hand(max_hand_length, eval)
        print()
    
    print("\033[F=========================================\n")