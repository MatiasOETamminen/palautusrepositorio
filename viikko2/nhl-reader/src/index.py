from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22",
    "2022-23", "2023-24", "2024-25", "2025-26"
]

NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
    "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
    "NOR", "UZB", "LAT", "AUS"
]

def main(): # pylint: disable=too-many-statements
    console = Console()

    console.print("Seasons:", "/".join(SEASONS))
    season = console.input("Season: ")
    while season not in SEASONS:
        season = console.input("Choose one of the listed seasons: ")

    # Ask whether the user wants to filter by nationality or by team
    filter_choice = console.input("Filter by nationality or team? [n/t]: ").strip().lower()
    while filter_choice not in ("n", "t"):
        filter_choice = console.input("Choose 'n' for nationality or 't' for team: ").strip().lower()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    if filter_choice == "n":
        console.print("Nationalities:", "/".join(NATIONALITIES))
        nationality = console.input("Nationality: ").upper()
        while nationality not in NATIONALITIES:
            nationality = console.input("Choose one of the listed nationalities: ").upper()

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Season {season} players from {nationality}")
        table.add_column("Released", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in players:
            points = player.goals + player.assists
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(points),
            )

        console.print(table)
    else:
        team = console.input("Team: ")
        team_players = stats.players_by_team(team)
        team_table = Table(title=f"Season {season} players from team {team}")
        team_table.add_column("name", style="cyan")
        team_table.add_column("team", style="magenta")
        team_table.add_column("goals", justify="right", style="green")
        team_table.add_column("assists", justify="right", style="green")
        team_table.add_column("points", justify="right", style="green")

        for player in team_players:
            points = player.goals + player.assists
            team_table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(points),
            )

        console.print(team_table)

if __name__ == "__main__":
    main()
