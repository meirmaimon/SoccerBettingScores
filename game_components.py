class Odd:

    def __init__(self, bookmaker, home_odd, away_odd, odd_type):
        self.bookmaker = bookmaker
        self.home_odd = home_odd
        self.away_odd = away_odd
        self.odd_type = odd_type


class H2HOdd(Odd):
    def __init__(self, bookmaker, home_odd, away_odd, draw_odd, odd_type):
        super().__init__(bookmaker, home_odd, away_odd, odd_type)
        self.draw_odd = draw_odd


class SpreadsOdd(Odd):
    def __init__(self, bookmaker, home_odd, away_odd, point_home, point_away, odd_type):
        super(SpreadsOdd, self).__init__(bookmaker, home_odd, away_odd, odd_type)
        self.home_point = point_home
        self.away_point = point_away



class Market:
    def __init__(self, market_type, odds):
        self.market_type = market_type
        self.market_odds = odds
        self.default_odd_value = 0

    def find_best(self):
        odd = self.market_odds[0]
        odd_attributes = [a for a in dir(odd) if
                          not a.startswith('__')
                          and not callable(getattr(odd, a))
                          and (type(getattr(odd, a)) == float)]
        odd_attributes_dict = dict.fromkeys(odd_attributes, (0, ""))
        for odd in self.market_odds:
            for odd_attr in odd_attributes:
                prev_odd_val = odd_attributes_dict.get(odd_attr)[0]
                cur_odd_val = getattr(odd, odd_attr)
                if cur_odd_val > prev_odd_val:
                    odd_attributes_dict[odd_attr] = (cur_odd_val, getattr(odd, "bookmaker"))
        return odd_attributes_dict


class Game:

    def __init__(self, home_team, away_team, date, markets: list[Market]):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.markets = markets
        self.best_odds = [market.find_best() for market in self.markets]


