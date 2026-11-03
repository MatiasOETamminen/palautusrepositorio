import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.response = requests.get(url).json()
        self.get_players()

    def get_players(self):
        self.players = []

        for player_dict in self.response:
            self.players.append(Player(player_dict))
