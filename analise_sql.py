import pandas as pd
import sqlite3

def run_query(query, conn):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Erro ao executar a query {e}")
        return None
    

conn = sqlite3.connect('spotify.db')    

print("--- Artistas mais Populares ---")
query1 = """
SELECT
    artist_name,
    AVG(popularity) AS Popularidade_media
FROM
    spotify
GROUP BY
    artist_name
ORDER BY
    Popularidade_media DESC;
"""

df_top_artistas = run_query(query1, conn)
print(df_top_artistas)

print("\n--- Top 10 Gêneros mais 'Dançantes' ---")
query2 = """
SELECT
    genre,
    AVG(danceability) AS Media_dancante
FROM
    spotify
GROUP BY
    genre
ORDER BY
    Media_dancante DESC
LIMIT
    10;
"""

df_top_dancantes = run_query(query2, conn)
print(df_top_dancantes)

print("\n--- Top Mais Energéticos: ---")
query3 = """
SELECT
    genre,
    AVG(energy) AS Media_energia
FROM
    spotify
GROUP BY 
    genre
ORDER BY
    Media_energia DESC
LIMIT
    10;
"""

df_top_energeticos = run_query(query3, conn)
print(df_top_energeticos)

print("\n--- Ranking das 20 Músicas mais Populares! ---")
query4 = """
SELECT
    track_name AS 'Música',
    artist_name AS 'Artista',
    popularity AS 'Pontuação'
FROM
    spotify
ORDER BY
    popularity DESC;
"""

df_top_mais_populares = run_query(query4, conn)
print(df_top_mais_populares)

print("\n--- Top Músicas Rap/Hip-Rop ---")
query5 = """
SELECT
    track_name AS 'Música',
    artist_name AS 'Artista',
    popularity AS 'Pontuação',
    genre AS 'Gênero'
FROM
    spotify
WHERE
    genre = 'Hip-Hop' OR genre = 'Rap'
ORDER BY
    popularity DESC
LIMIT
    20;
"""

df_top_20_rap_hip_rop = run_query(query5, conn)
print(df_top_20_rap_hip_rop)

conn.close()