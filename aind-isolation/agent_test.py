"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def time_left(self):
        return 10.
    
    def test_minimax(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2) 
        time_left = lambda : 10.
        print(self.player1.get_move(self.game, time_left))
        #winner, history, outcome = self.game.play()

    def test_alphabeta(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2) 
        time_left = lambda : 10.
        print(self.player1.get_move(self.game, time_left))
        #winner, history, outcome = self.game.play()

if __name__ == '__main__':
    unittest.main()
