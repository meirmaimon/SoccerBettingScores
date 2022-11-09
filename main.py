import games_data


def main():
    sport_info = games_data.get_games_data("soccer_spain_la_liga","us","h2h,spreads")
    games_list_formatted = games_data.format_game_data(sport_info)
    for game in games_list_formatted:
        print(f"away:{game.away_team},home:{game.home_team}:\n{game.best_odds}")


if __name__ == '__main__':
    main()
