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

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä

        Jos how_many on suurempi kuin pelaajien määrä, palautetaan kaikki pelaajat lajiteltuna.
        """
        players = list(self.reader.players)
        players = sorted(players, key=lambda p: p.goals, reverse=True)
        # Palauta haluttu määrä pelaajia
        return players[:how_many]

    def players_by_team(self, team: str):
        """Return all players who play for `team`, sorted by points (desc) and
        name (asc) as a secondary key.
        """
        players = [p for p in self.reader.players if p.team == team]
        # Sort by points descending, then name ascending
        players = sorted(players, key=lambda p: (-(p.goals + p.assists), p.name))
        return players
