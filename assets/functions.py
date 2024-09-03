from assets.leaguepedia_load import leaguepedia
from assets.fields import game_fields, tournaments_fields
from assets.normalize_games import *

def get_games(tournament_overview_page=None, **kwargs):
    games = leaguepedia.query(
        tables="ScoreboardGames",
        fields=", ".join(game_fields),
        where=f"ScoreboardGames.OverviewPage ='{tournament_overview_page}'",
        order_by="ScoreboardGames.DateTime_UTC",
        **kwargs,
    )

    normalize_games = normalize(games, tournament_overview_page)
    cleaned_games = remove_empty_keys(normalize_games)

    return cleaned_games

def get_league(
    region: str = None,
    year: int = None,
    tournament_level: str = "Primary",
    is_playoffs: bool = None,
    **kwargs,
    ):
 
    # We need to cast is_playoffs as an integer for the cargoquery
    if is_playoffs is not None:
        is_playoffs = 1 if is_playoffs else 0

    # This generates the WHERE part of the cargoquery
    where = " AND ".join(
        [
            # One constraint per variable
            f"Tournaments.{field_name}='{value}'"
            for field_name, value in [
                ("Region", region),
                ("Year", year),
                ("TournamentLevel", tournament_level),
                ("IsPlayoffs", is_playoffs),
            ]
            # We don’t filter on variables that are None
            if value is not None
        ]
    )

    result = leaguepedia.query(
        tables="Tournaments, Leagues",
        join_on="Tournaments.League = Leagues.League",
        fields=f"Leagues.League_Short, {', '.join(f'Tournaments.{field}' for field in tournaments_fields)}",
        where=where,
        **kwargs,
    )

    return result

def get_regions():
    regions_dicts_list = leaguepedia.query(
        tables="Tournaments", fields="Region", group_by="Region"
    )

    return [row["Region"] for row in regions_dicts_list]
