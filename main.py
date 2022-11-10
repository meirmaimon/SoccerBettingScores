import games_data


def main():
    sport_info = games_data.get_games_data("soccer_spain_la_liga","us","h2h,spreads")
    games_list_formatted = games_data.create_game_list(sport_info)
    for game in games_list_formatted:
        print(f"Away: {game.away_team},Home: {game.home_team}:\n")
        for odd in game.best_odds:
            print(f"{odd}\n")


if __name__ == '__main__':
    main()
