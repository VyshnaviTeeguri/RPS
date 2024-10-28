# test_module.py

import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class TestRPS(unittest.TestCase):
    def test_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreater(result["player"], result["quincy"])

    def test_abbey(self):
        result = play(player, abbey, 1000)
        self.assertGreater(result["player"], result["abbey"])

    def test_kris(self):
        result = play(player, kris, 1000)
        self.assertGreater(result["player"], result["kris"])

    def test_mrugesh(self):
        result = play(player, mrugesh, 1000)
        self.assertGreater(result["player"], result["mrugesh"])

if __name__ == "__main__":
    unittest.main()
