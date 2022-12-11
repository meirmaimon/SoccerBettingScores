"""
This module contains all games components classes.

Classes:
    Odd
    H2HOdd
    SpreadsOdd
    Game
    Market
"""

from dataclasses import dataclass, field


@dataclass
class Odd:
    bookmaker: str
    home_odd: float
    away_odd: float


@dataclass
class H2HOdd(Odd):
    draw_odd: float
    odd_type: str


@dataclass
class SpreadsOdd(Odd):
    home_point: float
    away_point: float
    odd_type: str


@dataclass
class BookmakerOffer:
    bookmaker: str
    offer: float


@dataclass
class MultyBookmakerOdd:
    home_odd: float
    away_odd: float
    home_bookmaker: str
    away_bookmaker: str


@dataclass
class MultyBookmakerH2HOdd(MultyBookmakerOdd):
    draw_odd: float
    draw_bookmaker: str
    odd_type: str


@dataclass
class MultyBookmakerSpreadsOdd(MultyBookmakerOdd):
    home_point: float
    away_point: float
    odd_type: str


@dataclass
class Market:
    market_type: str
    market_odds: list[Odd]
    best_odds: MultyBookmakerOdd = field(default=None)

    def set_market_best_multy_bookmaker_odds(self, best_odd: MultyBookmakerOdd):
        self.best_odds = best_odd


@dataclass
class Game:
    home_team: str
    away_team: str
    date: str
    markets: list[Market]
