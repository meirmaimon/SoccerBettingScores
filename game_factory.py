"""
This module is a Factory module to create the game components.
implements a basic factory that create an object given needed parameters.
Classes:
    GameFactory
"""
from game_components import *

class GameFactory:
    @staticmethod
    def create_odd(market_type, outcomes_odds, home_team, away_team, bookmaker):
        if market_type == 'h2h' or market_type == 'h2h_lay':
            home_odd = next(odd['price'] for odd in outcomes_odds if odd['name'] == home_team)
            away_odd = next(odd['price'] for odd in outcomes_odds if odd['name'] == away_team)
            draw_odd = next(odd['price'] for odd in outcomes_odds if odd['name'] == "Draw")
            return H2HOdd(bookmaker, home_odd, away_odd, draw_odd, market_type)
        elif market_type == 'spreads':
            home_odd = next(odd['price'] for odd in outcomes_odds if odd['name'] == home_team)
            away_odd = next(odd['price'] for odd in outcomes_odds if odd['name'] == away_team)
            home_point = next(odd['point'] for odd in outcomes_odds if odd['name'] == home_team)
            away_point = next(odd['point'] for odd in outcomes_odds if odd['name'] == away_team)
            return SpreadsOdd(bookmaker, home_odd, away_odd, home_point, away_point, market_type)
        else:
            raise Exception("Invalid odd format")

    @staticmethod
    def create_markets(odd_list: Odd):
        markets_types = {}
        for odd in odd_list:
            markets_types.setdefault(odd.odd_type, []).append(odd)
        return [Market(k, v) for (k, v) in markets_types.items()]

    @staticmethod
    def create_game(home_team,away_team,date,markets):
        return Game(home_team,away_team,date,markets)
