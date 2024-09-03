from assets.functions import get_league, get_games
from get_tournament import get_league_names
from pprint import pprint

def generate_top4_per_year(year_nro, create_csv):
    if int(year_nro) > 2022:
        top4_names = ['Korea', 'China', 'EMEA', 'North America']
    else:
        top4_names = ['Korea', 'China', 'Europe', 'North America']
    top4_tournament_array = [get_league(leagues, year=year_nro) for leagues in top4_names]
    top4_leagues_overview_name = [get_league_names(ligas) for ligas in top4_tournament_array]

    for regions in top4_leagues_overview_name:
        for league_name in regions:
            games = get_games(league_name)

            if not games:  # if not exist
                print(f"No games found for league: {league_name}")
                continue  # Pass to next league
            
            create_csv(games, league_name)



def generate_region_last5year(region, create_csv):
    years = ["2020", "2021", "2022", "2023", "2024"]
    leagues_overview = []
    for find_year in years:
        if region == 'EMEA' and int(find_year) <= 2022:
            current_region = 'Europe'
        else:
            current_region = region
        
        # Obtener torneos para la región y el año actuales
        top4_tournament_array = get_league(current_region, year=find_year)
        
        # Obtener nombres de ligas
        leagues_overview.append(get_league_names(top4_tournament_array))
    
    for regions in leagues_overview:
        for league_name in regions:
            games = get_games(league_name)

            if not games:  # if not exist
                print(f"No games found for league: {league_name}")
                continue  # Pass to next league
            
            create_csv(games, league_name)

