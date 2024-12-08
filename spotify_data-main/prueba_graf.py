import pandas as pd
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt

# Nombre del archivo CSV en la misma carpeta que el script
file_name = "spotify.csv"

# Carga el archivo CSV en un DataFrame usando el separador correcto
try:
    df = pd.read_csv(file_name, sep=";")
except FileNotFoundError:
    print(f"Error: El archivo '{file_name}' no se encontró.")
    exit()

# Verifica las columnas del archivo
print("Columnas disponibles en el archivo:")
print(df.columns)

# Procesa la columna 'date' para asegurarte de que tiene el formato correcto
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
else:
    print("\nLa columna 'date' no existe en el archivo. No se puede continuar con el análisis de años.")
    exit()

# Filtra el DataFrame para el año actual
current_year = datetime.now().year
df['year'] = df['date'].dt.year
filtered_df = df[df['year'] == current_year]

# Cuenta las canciones
if 'song' in df.columns:
    song_counts = Counter(filtered_df['song'])

    # Extrae las 10 canciones más escuchadas
    top_10_songs = song_counts.most_common(10)

    # Imprime las canciones y sus conteos
    print("\nTop 10 canciones más escuchadas:")
    for song, count in top_10_songs:
        print(f"{song}: {count} reproducciones")

    # Genera la gráfica
    songs = [song for song, count in top_10_songs]
    counts = [count for song, count in top_10_songs]

    plt.figure(figsize=(10, 6))
    plt.barh(songs, counts, color='skyblue')
    plt.xlabel("Reproducciones")
    plt.ylabel("Canciones")
    plt.title(f"Top 10 canciones más escuchadas en {current_year}")
    plt.gca().invert_yaxis()  # Invierte el eje Y para que la más popular esté arriba
    plt.tight_layout()
    plt.show()

else:
    print("\nLa columna 'song' no existe en el archivo.")
