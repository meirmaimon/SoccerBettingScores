"""This class used for fetching
sports betting data
using https://api.the-odds-api.com API"""

import requests
import config
from game_factory import *

API_SOCCER_KEY = config.api_soccer_key
API_SPORT = 'https://api.the-odds-api.com/v4/sports'


def get_sport_key_list():
    """
    Gets a list with sport types keys that has odds data.
    :return: List with sport types keys that has odds data.
    """
    param = {"api_key": API_SOCCER_KEY}
    res = requests.get(API_SPORT, param)
    res.raise_for_status()
    sport_types = res.json()
    # return sport_types
    return [sport_type['key'] for sport_type in sport_types]


def get_games_data(sport_type, regions, markets='h2h'):
    """
    Get betting data on sport given
    :param sport_type: the sport type
    :param regions: regions of bookmakers , valid regions - us,uk,au,eu
    :param markets: markets of odd - default is h2h
    :return: betting data on the given sport
    """
    param = {"sport": sport_type, "api_key": API_SOCCER_KEY, "regions": regions, "markets": markets}
    api_soccer_odds = f"{API_SPORT}/{sport_type}/odds"

    res = requests.get(api_soccer_odds, params=param)
    res.raise_for_status()
    return res.json()


def create_game_list(sport_info):
    """
    Create list of all the games from the sport data given by the API
    :param sport_info: betting data fetched from odd_API
    :return: list of games with theirs betting data
    """
    games_list = []
    # Get teams name and game time
    for game_info in sport_info:
        home_team = game_info['home_team']
        away_team = game_info['away_team']
        game_date = game_info['commence_time']
        # Get Game odds
        markets_odds = []
        for bookmaker in game_info['bookmakers']:
            bookmaker_title = bookmaker['title']
            for market in bookmaker['markets']:
                market_type = market['key']
                outcomes_odds = market['outcomes']
                current_odd = GameFactory.create_odd(market_type, outcomes_odds, home_team, away_team, bookmaker_title)
                markets_odds.append(current_odd)
        # Create markets from the odds list
        markets = GameFactory.create_markets(markets_odds)
        # Create Market Best MultyBookmakerOdd
        for market in markets:
            market.set_market_best_multy_bookmaker_odds(create_market_best_multy_bookmaker_odds(market))
        # Create Game
        games_list.append(GameFactory.create_game(home_team, away_team, game_date, markets))
    return games_list


def create_market_best_multy_bookmaker_odds(market: Market):
    odd = market.market_odds[0]
    odd_attributes = [a for a in dir(odd) if
                      not a.startswith('__')
                      and not callable(getattr(odd, a))
                      and (type(getattr(odd, a)) == float)]
    odd_attributes_dict = dict.fromkeys(odd_attributes, BookmakerOffer("", float("-inf")))
    for odd in market.market_odds:
        for odd_attr in odd_attributes:
            prev_odd_val = odd_attributes_dict.get(odd_attr).offer
            cur_odd_val = getattr(odd, odd_attr)
            if cur_odd_val > prev_odd_val:
                odd_attributes_dict[odd_attr] = BookmakerOffer(getattr(odd, "bookmaker"), cur_odd_val)
    return GameFactory.create_multy_bookmaker_odd(market.market_type, odd_attributes_dict)
