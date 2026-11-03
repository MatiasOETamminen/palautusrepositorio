class Player: # pylint: disable=too-few-public-methods
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.assists = dictionary['assists']
        self.goals = dictionary['goals']
        self.team = dictionary['team']
        self.games = dictionary['games']
        self.id = dictionary['id']

    def __str__(self):
        return f"{self.name:20}" + f"{self.team:20}" + f"{self.goals}"\
        + " + " + f"{self.assists}" + " = " + f"{self.goals + self.assists}"
