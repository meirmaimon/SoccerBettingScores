from games_data import *
from betting_calculator import *


def main():
    # print(get_sport_key_list())
    sport_info = get_games_data('soccer_fifa_world_cup', "uk,eu", "h2h")
    games_list_formatted = create_game_list(sport_info)
    for game in games_list_formatted:
        print(f"Away: {game.away_team},Home: {game.home_team}")
        for market in game.markets:
            print(market.best_odds)
        print(find_arbitrage(game))


if __name__ == '__main__':
    main()
