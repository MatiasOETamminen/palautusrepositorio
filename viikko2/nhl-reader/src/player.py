class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name:20}" + f"{self.team:20}" + f"{self.goals}"\
        + " + " + f"{self.assists}" + " = " + f"{self.goals + self.assists}" 
