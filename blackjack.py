from src.deck import Deck
from src.hand import Hand
from src.dealer import Dealer
from src.player import Player, print_state


def play():
    #instantiate the deck and shuffle it
    deck = Deck()
    deck.shuffle()

    #get the number of players
    num_players = get_number("Enter the number of players: ", "Please enter an integer between 1 and 3 inclusive.", [1, 3])
    print()

    players = []
    dealer  = Dealer()

    #instantiate the players array with Player objects
    for i in range(num_players):
        num_hands = get_number(f"Enter the number of hands for Player {i+1}: ", "Please enter an integer between 1 and 3 inclusive.", [1, 3])

        players.append(Player(num_hands))

    #game loop
    while True:
        #populate each hand with two cards from the deck
        for _ in range(2):
            for player in players:
                for hand in player.hands:
                    card_drawn = deck.draw_card()
                    hand.hit(card_drawn)
            
            card_drawn = deck.draw_card()
            dealer.hit(card_drawn)

        #keep track of the number of cards the longest hand has
        #this is used to display the state of the game consistently
        max_hand_length = 2

        #allow each player to play out their hands
        for i in range(num_players):
            max_hand_length = players[i].play_hands(i, players, dealer, deck, max_hand_length)

        #display the current state of the game 
        print_state(players, dealer, max_hand_length)

        #play out the dealer's hand
        max_hand_length = dealer.play_hand(deck, max_hand_length)

        #threshold will store the dealer's final score or -1 if the dealer bust
        threshold =  -1
        if dealer.score[0] <= 21:
            threshold = dealer.score[0]

        #evaluate each player's hands
        for player in players:
            for hand in player.hands:
                hand.evaluate(threshold)

        #display the state of the game
        print_state(players, dealer, max_hand_length, True)

        #if the user wants to play again
        if play_again() == True:
            #reset the game
            dealer = Dealer()
            
            for i in range(num_players):
                for j in range(len(players[i].hands)):
                    players[i].hands[j] = Hand()
        else:
            break

def get_number(message, warning, bounds):
    """
    Prompt the user to input an integer between the bounds.
    
    Parameters:
        message (str): the message to display to the user when requesting input
        warning (str): the message to display to the user when their input is invalid
        bound (List[int]): the upper and lower bounds of the integer

    Returns:
        int: A valid integer within the bounds
    """

    while True:
        try:
            #get user input
            num = int(input(message).strip())
            
            #input validation
            if num < bounds[0] or num > bounds[1]:
                print(warning)
            else:
                return num
        except ValueError:
            print(warning)

        
def play_again():
    """
    Ask the user whether they want to play again and return their response as a boolean.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """

    while True:
        #get user input
        action = input(f"Would you like to play again? (yes/no): ").strip().lower()
            
        #convert input to boolean
        if action == "yes":
            return True
        elif action == "no":
            return False
        
        #let user try again
        print("Please choose between yes or no.")


if __name__ == '__main__':
    play()
