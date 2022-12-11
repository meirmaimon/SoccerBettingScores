from game_components import Game, MultyBookmakerH2HOdd
from game_factory import GameFactory


def find_margin(outcomes: list):
    return sum(map(lambda x: 1 / x, outcomes)) * 100


def find_arbitrage(game: Game):
    for market in game.markets:
        if market.market_type == "h2h":
            market_multy_odd = market.best_odds
            margin = find_margin(GameFactory.create_outcomes_list(market_multy_odd))
            if margin < 100:
                return margin, calc_bets_to_put(market_multy_odd, 1000)


def calc_bets_to_put(multy_odd, amount):
    if multy_odd.odd_type == 'h2h':
        home_bet_amount = (amount / (
                1 + (multy_odd.home_odd / multy_odd.draw_odd) + (multy_odd.home_odd / multy_odd.away_odd)))
        draw_bet_amount = (amount / (
                1 + (multy_odd.draw_odd / multy_odd.home_odd) + (multy_odd.draw_odd / multy_odd.away_odd)))
        away_bet_amount = (amount / (
                1 + (multy_odd.away_odd / multy_odd.home_odd) + (multy_odd.away_odd / multy_odd.draw_odd)))
        return {"home": home_bet_amount, "away": away_bet_amount, "draw": draw_bet_amount}
