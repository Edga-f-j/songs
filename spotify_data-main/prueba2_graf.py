import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from collections import Counter

# Nombre del archivo CSV en la misma carpeta que el script
file_name = "spotify.csv"

# Carga el archivo CSV en un DataFrame usando el separador correcto
df = pd.read_csv(file_name, sep=";")

# Obtiene la fecha y el mes actual
current_datetime = datetime.now()
current_month = current_datetime.strftime("%B")  # Computa automáticamente el mes actual

# Contador de artistas y canciones
counts_artist = Counter(df['artist'])
counts_song = Counter(df['song'])

# Filtra los datos para el mes actual (si contiene el mes en el campo 'date')
wrapped = df[df['date'].str.contains(f'{current_month}', na=False)]

# Información general de escucha
print(f"\nI LISTENED TO {len(counts_artist.items())} DIFFERENT ARTISTS IN 2024\n")
print(f"I LISTENED TO {len(wrapped)} SONGS IN 2024 (ROUGHLY {3*len(wrapped)} MINUTES OR {3*len(wrapped) / 60} HOURS OR {3*len(wrapped) / 60 / 60} DAYS) \n")
print(f"I LISTENED TO {len(counts_song.items())} DIFFERENT SONGS IN 2024\n")

# Muestra estadísticas generales
print("_________________________________________________________\n")

# Filtra los artistas y canciones más escuchados
most_popular_artist = {key: value for key, value in counts_artist.items() if value >= 10}
most_popular_song = {key: value for key, value in counts_song.items() if value >= 15}

# Ordena los artistas y canciones por número de reproducciones (de mayor a menor)
most_popular_artist = dict(sorted(most_popular_artist.items(), key=lambda x: x[1], reverse=True))
most_popular_song = dict(sorted(most_popular_song.items(), key=lambda x: x[1], reverse=True))

# Obtiene los 10 artistas y canciones más populares
keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

# Gráfica de los 10 artistas más populares
plt.figure(figsize=(10, 6))
sns.barplot(x=values_list_artist[:10], y=keys_list_artist[:10], palette="Blues_d")
plt.title('Top 10 Artists in 2024', fontsize=16)
plt.xlabel('Number of Plays')
plt.ylabel('Artist')
plt.show()

keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

# Gráfica de las 10 canciones más populares
plt.figure(figsize=(10, 6))
sns.barplot(x=values_list_song[:10], y=keys_list_song[:10], palette="Greens_d")
plt.title('Top 10 Songs in 2024', fontsize=16)
plt.xlabel('Number of Plays')
plt.ylabel('Song')
plt.show()

# Muestra canciones y artistas escuchados solo una vez
most_popular_artist = {key: value for key, value in counts_artist.items() if value == 1}
most_popular_song = {key: value for key, value in counts_song.items() if value == 1}

# Ordena de nuevo los artistas y canciones que fueron escuchados solo una vez
most_popular_artist = dict(sorted(most_popular_artist.items(), key=lambda x: x[1], reverse=True))
most_popular_song = dict(sorted(most_popular_song.items(), key=lambda x: x[1], reverse=True))

keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

print("\n")
print(f"I LISTENED TO {len(keys_list_artist)} ARTISTS ONLY ONE TIME IN 2024")
print(f"I LISTENED TO {len(keys_list_song)} SONGS ONLY ONE TIME IN 2024")
print("\n")

# Conteo de un artista específico (ejemplo: Taylor Swift)
artist_counts = Counter(wrapped['artist'])
count_taylor_swift = artist_counts["Taylor Swift"]  # Puedes cambiar "Taylor Swift" por cualquier artista
print(f"TAYLOR SWIFT COUNT: {count_taylor_swift}")
