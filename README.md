# leaguepedia_games_csv

**leaguepedia_games_csv** es una herramienta para extraer y almacenar datos de las partidas competitivas de League of Legends en un archivo `.csv` con encabezados organizados.

## Características

- **Fuente de datos:** Utiliza [CargoQuery](https://lol.fandom.com/wiki/Special:CargoQuery) de LoL Fandom.
- **Normalización:** El programa también normaliza algunos datos para mantener la consistencia.

## Datos Extraídos

El programa extrae los siguientes datos para cada partida:

- **Team1**
- **Team2**
- **WinTeam**
- **LossTeam**
- **DateTime_UTC**
- **Team1Score**
- **Team2Score**
- **Winner**
- **Gamelength**
- **Gamelength_Number**
- **Team1Bans**
- **Team2Bans**
- **Team1Picks**
- **Team2Picks**
- **Team1Players**
- **Team2Players**
- **Team1Dragons**
- **Team2Dragons**
- **Team1Barons**
- **Team2Barons**
- **Team1Towers**
- **Team2Towers**
- **Team1Gold**
- **Team2Gold**
- **Team1Kills**
- **Team2Kills**
- **Team1RiftHeralds**
- **Team2RiftHeralds**
- **Team1VoidGrubs**
- **Team2VoidGrubs**
- **Team1Inhibitors**
- **Team2Inhibitors**
- **Patch**
- **GameId**

## Normalización de Datos

Además de la extracción, el programa normaliza ciertos datos en la tabla para mejorar la consistencia y facilitar su análisis posterior.

---

## Uso

Para utilizar este programa, simplemente ejecuta main.py y los datos se guardarán automáticamente en el archivo `.csv` dentro de la carpeta `Dataset`.

---


## Licencia

Este proyecto está bajo la licencia MIT.
