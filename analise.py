import pandas as pd
import sqlite3

try:
    df = pd.read_csv("SpotifyFeatures.csv")
    print("Arquivo carregado com sucesso!")
except FileNotFoundError:
    print("Err: Arquivo não foi encontrado!")

db_nome = 'spotify.db'
conn = sqlite3.connect(db_nome)
print(f"Banco '{db_nome}' criado com sucesso!")

df.to_sql('spotify', conn, if_exists = 'replace', index = False)

conn.close()
