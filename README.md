# Blackjack Game

This project is an implementation of a Blackjack game in Python. 
It includes classes for the deck, hand, player, and dealer, as well as a game loop to play the game. 
The project also includes unit tests for the main components.

## Getting Started

### Prerequisites
- Python 3.x

### Running the Game
To run the game, execute the following command in your terminal:

```sh
python3 blackjack.py
```

### Running the Tests
To run the unit tests, execute the following command in your terminal:

```sh
python3 -m unittest discover test
```

## Project Structure
The project consists of the following files and directories:

- **`blackjack.py`**: The main script to run the game.
- **`src/`**: Contains the source code for the game.
  - **`dealer.py`**: Contains the `Dealer` class.
  - **`deck.py`**: Contains the `Deck` class.
  - **`hand.py`**: Contains the `Hand` class.
  - **`player.py`**: Contains the `Player` class.
- **`test/`**: Contains the unit tests for the game.
  - **`test_dealer.py`**: Unit tests for the `Dealer` class.
  - **`test_deck.py`**: Unit tests for the `Deck` class.
  - **`test_hand.py`**: Unit tests for the `Hand` class.
  - **`test_player.py`**: Unit tests for the `Player` class.

## How to Play
1. Run the game using the command mentioned above.
2. Follow the prompts to enter the number of players and the number of hands for each player.
3. The game will deal cards to the players and the dealer.
4. Players will be prompted to `hit`, `stand`, or `split` (if possible).
5. The dealer will play their hand according to the standard rules.
6. The game will evaluate the hands and display the results.
7. You will be prompted to play again or exit the game.
