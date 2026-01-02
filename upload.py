import pandas as pd
import sqlite3

# conectar o banco de dados
conn = sqlite3.connect("spotify.db")

# executar o upload dos dados
files = {
    "artists": "spotify_artist_data_2023.csv",
    "features": "spotify_features_data_2023.csv",
    "tracks": "spotify_tracks_data_2023.csv",
    "albums": "spotify-albums_data_2023.csv",
}

for table, path in files.items():
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="replace", index=False)

# desconectar o banco de dados
conn.close()
