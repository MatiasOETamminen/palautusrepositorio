class TennisGame:
    SCORES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score_difference(self):
        return self.player1_score - self.player2_score

    def has_player_reached_four_points(self):
        return max(self.player1_score, self.player2_score) >= 4

    def get_leading_player(self):
        if self.get_score_difference() > 0:
            return "player1"
        elif self.get_score_difference() < 0:
            return "player2"
        else:
            return None

    def get_score(self):
        if self.get_score_difference() == 0:
            if self.player1_score < 3:
                score = TennisGame.SCORES[self.player1_score] + "-All"
            else:
                score = "Deuce"
        elif self.has_player_reached_four_points():
            if abs(self.get_score_difference()) == 1:
                score = "Advantage " + self.get_leading_player()
            else:
                score = "Win for " + self.get_leading_player()
        else:
            score = TennisGame.SCORES[self.player1_score] + "-" + TennisGame.SCORES[self.player2_score]
        return score
