# Tests for src/player_stats.py
import os
import sys
import pytest

# Ensure the project root is on sys.path so `src` can be imported when running pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.player import Player
from src.player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self.players = players


def make_player(name, nationality, team, goals, assists):
    return Player({
        'name': name,
        'nationality': nationality,
        'assists': assists,
        'goals': goals,
        'team': team,
        'games': 0,
        'id': 0,
    })


def test_top_scorers_by_nationality_orders_by_points_desc():
    p1 = make_player('Player A', 'FIN', 'T1', 10, 5)   # 15
    p2 = make_player('Player B', 'FIN', 'T2', 8, 10)   # 18
    p3 = make_player('Player C', 'SWE', 'T1', 20, 0)   # 20

    reader = StubReader([p1, p2, p3])
    stats = PlayerStats(reader)

    result = stats.top_scorers_by_nationality('FIN')

    assert [p.name for p in result] == ['Player B', 'Player A']


def test_top_goal_scorers_limits_and_order():
    p1 = make_player('A', 'AAA', 'X', 5, 0)
    p2 = make_player('B', 'BBB', 'Y', 10, 0)
    p3 = make_player('C', 'CCC', 'Z', 7, 0)

    reader = StubReader([p1, p2, p3])
    stats = PlayerStats(reader)

    top2 = stats.top_goal_scorers(2)
    assert [p.name for p in top2] == ['B', 'C']

    # If how_many is larger than player count, all players are returned (sorted)
    all_players = stats.top_goal_scorers(10)
    assert [p.name for p in all_players] == ['B', 'C', 'A']

    # how_many == 0 -> empty list
    none_players = stats.top_goal_scorers(0)
    assert none_players == []


def test_players_by_team_sorted_by_points_then_name():
    # Two players with same points but different names
    p1 = make_player('Zed', 'X', 'TeamX', 5, 5)   # 10 points
    p2 = make_player('Anna', 'Y', 'TeamX', 6, 4)  # 10 points
    p3 = make_player('Bob', 'Y', 'TeamX', 4, 3)   # 7 points
    p4 = make_player('Other', 'Z', 'OtherTeam', 100, 0)

    reader = StubReader([p1, p2, p3, p4])
    stats = PlayerStats(reader)

    team_players = stats.players_by_team('TeamX')

    # Points: Anna(10), Zed(10) -> tie broken by name (Anna before Zed), then Bob
    assert [p.name for p in team_players] == ['Anna', 'Zed', 'Bob']


def test_players_by_team_no_players_returns_empty():
    reader = StubReader([])
    stats = PlayerStats(reader)
    assert stats.players_by_team('NonExistent') == []
