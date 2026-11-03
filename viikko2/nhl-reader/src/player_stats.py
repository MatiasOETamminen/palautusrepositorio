class PlayerStats: # pylint: disable=too-few-public-methods
    def __init__(self, reader: "PlayerReader"):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = []
        for player in self.reader.players:
            if player.nationality == nationality:
                players.append(player)

        players = sorted(players,
                        key=lambda player: player.goals + player.assists,
                        reverse=True)

        return players
