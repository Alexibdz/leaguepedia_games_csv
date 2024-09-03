import os 
def create_path(path):
    parts = path.split('/')
    season_parts = parts[1].split(' ')
    parts[1] = f'{season_parts[1]} {season_parts[0]}'
    
    file_path = f'Dataset/{parts[0]}/{parts[1]}/{parts[2]}.csv'

    # Crear los directorios si no existen
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    print(f"Datos guardados en {os.path.abspath(file_path)}")

    return file_path