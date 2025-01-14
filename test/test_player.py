import unittest
from src.player import Player


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player(3)

    def tearDown(self):
        pass

    '''''''''Split test'''''''''
    def test_split_first_hand(self):
        #add two cards with the same rank to the same hand
        self.player.hands[0].hit("A♣")
        self.player.hands[0].hit("A♦")
        
        #split said hand
        self.player.split(0)

        #check that the cards were distributed properly
        self.assertEqual(self.player.hands[0].cards, ["A♣"])
        self.assertEqual(self.player.hands[1].cards, ["A♦"])

        #check if the hand was appended without replacing any of the other hands
        self.assertEqual(len(self.player.hands), 4)

    def test_split_middle_hand(self):
        #add two cards with the same rank to the same hand
        self.player.hands[1].hit("A♣")
        self.player.hands[1].hit("A♦")
        
        #split said hand
        self.player.split(1)

        #check that the cards were distributed properly
        self.assertEqual(self.player.hands[1].cards, ["A♣"])
        self.assertEqual(self.player.hands[2].cards, ["A♦"])

        #check that the cards were distributed properly
        self.assertEqual(len(self.player.hands), 4)

    def test_split_last_hand(self):
        #add two cards with the same rank to the same hand
        self.player.hands[2].hit("A♣")
        self.player.hands[2].hit("A♦")
        
        #split said hand
        self.player.split(2)

        #check that the cards were distributed properly
        self.assertEqual(self.player.hands[2].cards, ["A♣"])
        self.assertEqual(self.player.hands[3].cards, ["A♦"])

        #check that the cards were distributed properly
        self.assertEqual(len(self.player.hands), 4)


if __name__ == '__main__':
    unittest.main()
