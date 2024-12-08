import pandas as pd
from datetime import datetime
from collections import Counter

# !!!!!! IMPORTANTE !!!!!!
# cambiar el nombre de la hoja de datos
file_name = "spotify.csv"

# con esto se guarda la hoja de datos en la una variable "df" 
# y la funcion del "sep=';' es separar los datos por ese ';'"
# la funcion del try ... except no es algo necesario para que sirva el codigo
# solo es que en caso de que no sirva muestre ese mensaje de error
try:
    df = pd.read_csv(file_name, sep=";")
except FileNotFoundError:
    print(f"Error: El archivo '{file_name}' no se encontró.")
    exit()

# este codigo no es escencial, es solo para  verificar que las columnas 
# si las reconoce el codigo
print("Columnas disponibles en el archivo:")
print(df.columns)


# jaja otra vez, esta seccion no es tan escencial
if 'song' in df.columns:
    print("\nLista de canciones en la columna 'song':")
    print(df['song'])
else:
    print("\nLa columna 'song' no existe en el archivo.")
    exit()



# OJOOO!! este codigo tambien es de verificacion pero si es importante porque cambia el estilo de las fechas
# para que el codigo si las pueda leer, entonces la funcion como tal es:
# Verifica si la columna date existe.
# Convierte los datos de esta columna en fechas usando pd.to_datetime().
# Si hay un error en alguna fecha, la convierte en NaT (valor nulo para fechas).
# Si no encuentra la columna, muestra un mensaje y termina el programa.
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Convierte a formato datetime
    print("\nFechas procesadas correctamente.")
else:
    print("\nLa columna 'date' no existe en el archivo. No se puede continuar con el análisis de años.")
    exit()



#esta linea de codigo literalmente iguala 'current_year' a 2024, ese codigo 'datetime.now().year'
# es para que el mismo codigo detecte el año en el que estamos, osea que solo vamos a tomar los datos
# del año 2024
current_year = datetime.now().year


# el coodigo de ' df['year'] = df['date'].dt.year' hace lo siguiente
# Crea una nueva columna llamada year en el DataFrame df.
# Extrae el año de cada fecha en la columna date usando .dt.year.
# Cómo funciona:
# df['date'] es una columna de tipo fecha y hora (datetime).
# df['date'].dt permite acceder a propiedades de fechas como el año (year), mes (month) o día (day).
# Después de ejecutar df['year'] = df['date'].dt.year   hace que se cree una nuevo columna que contenga solo el año
df['year'] = df['date'].dt.year
filtered_df = df[df['year'] == current_year]




# Cuenta artistas y canciones
#filtered_df['artist'] extrae el nombre de los artistas y luego con el 
# Counter cuenta cuantas veces aparece cada artista, igual pasa con las canciones
if 'artist' in df.columns and 'song' in df.columns:
    artist_counts = Counter(filtered_df['artist'])
    song_counts = Counter(filtered_df['song'])



    # Imprime estadísticas básicas
    print(f"\nEstadísticas de canciones escuchadas en {current_year}:")
    print(f"- Total de canciones: {len(filtered_df)}")
    print(f"- Artistas únicos: {len(artist_counts)}")
    print(f"- Canciones únicas: {len(song_counts)}")

    # Top 10 artistas más escuchados
    print("\nTop 10 artistas más escuchados:")
    for artist, count in artist_counts.most_common(10):
        print(f"{artist}: {count} reproducciones")

    # Top 10 canciones más escuchadas
    print("\nTop 10 canciones más escuchadas:")
    for song, count in song_counts.most_common(10):
        print(f"{song}: {count} reproducciones")
else:
    print("\nNo se encontraron las columnas 'artist' o 'song' necesarias para el análisis.")
