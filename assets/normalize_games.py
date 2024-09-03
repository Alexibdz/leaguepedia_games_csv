def clean_players_name(data):
    for key in data.keys():
        if key == 'Team1Players':
            data[key] = ','.join([player.split('(')[0].strip() for player in data[key].split(',')])
        if key == 'Team2Players':
            # Eliminar paréntesis y su contenido
            data[key] = ','.join([player.split('(')[0].strip() for player in data[key].split(',')])
    return data

def split_datetime(data):
    if 'DateTime UTC' in data:
        # Divide la fecha y la hora
        date_time = data['DateTime UTC'].split(' ')
        data['DateTime'] = date_time[0]  # Asigna la fecha a 'DateTime'
        data['UTC'] = date_time[1]       # Asigna la hora a 'UTC'
        
        # Elimina la clave original 'DateTime UTC'
        del data['DateTime UTC']
        del data['DateTime UTC__precision']
    return data

def clean_gameid_column(data, league_name):
    if 'GameId' in data:
        # Divide la fecha y la hora
        data['GameId'] = data['GameId'].replace(f"{league_name}_", '').strip('_')
        ids = data['GameId'].split('_')
        data['Stage'] = ids[0]
        data['StageMatchId'] = ids[1]
        data['StageMatchGameId'] = ids[2]

        del data['GameId']

    return data

def normalize(data, league_name):
    for idx, match in enumerate(data):
        clean_players_name(match)  # Elimina () / nombre completo del jugador
        split_datetime(match)      # Divide en dos columnas date_time
        clean_gameid_column(match, league_name)  # Limpia full_name_tournament y divide en tres columnas de ID (Stage, Stage_matchid, Stage_match_gameid)
        match['GameN'] = f"{idx + 1}"
        
    return data

def remove_empty_keys(data):
    # Recorre todos los elementos en la lista de diccionarios
    for item in data:
        # Comprueba si todas las columnas (valores) están vacías
        if all(not value for value in item.values()):
            # Crea una lista de claves para eliminar después para evitar modificar el diccionario mientras se itera
            keys_to_remove = list(item.keys())
            
            # Elimina todas las claves si todas las columnas están vacías
            for key in keys_to_remove:
                del item[key]
    
    return data
