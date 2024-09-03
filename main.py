import csv
from pprint import pprint
from assets.path import create_path
from get_top4_regions_dataset import generate_top4_per_year, generate_region_last5year

def create_csv(games_array, league_name):
    file_path = create_path(league_name)

    #generar encabezado
    headers = games_array[0].keys()
    # Escribe los datos en un archivo CSV
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Escribir encabezados
        writer.writerows(games_array)  # Escribir las filas de datos

#('Korea', 'China', 'North America', 'EMEA' or Europe (2022 and before)) 
#generate_top4_per_year("2021", create_csv) 
generate_region_last5year("Korea", create_csv)
