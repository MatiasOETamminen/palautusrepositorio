import requests
from player import Player

class PlayerReader: # pylint: disable=too-few-public-methods
    def __init__(self, url: str):
        self.response = requests.get(url, timeout=5).json()
        self.get_players()

    def get_players(self):
        self.players = []

        for player_dict in self.response:
            self.players.append(Player(player_dict))
