import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko").points, 16)

    def test_search_none(self):
        self.assertEqual(self.stats.search("asd"), None)

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_top(self):
        self.assertEqual(self.stats.top(3)[0].points, 124)
