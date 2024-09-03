from assets.functions import get_league, get_regions


def get_league_names(tournaments):
    search_names = []
    for tournament in tournaments:
        if 'OverviewPage' in tournament.keys():
            if '/' in tournament['OverviewPage']:
                search_names.append(tournament['OverviewPage'])
    return search_names


tournaments = get_league("China", year=2021)  #must include league name from get_regions() and a year

list_league = get_league_names(tournaments) #to get overview name for games
