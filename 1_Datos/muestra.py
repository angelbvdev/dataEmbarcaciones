import pandas as pd
# === 1. Cargar el dataset ===
file_path = "01_ENYE_ENE_2025.csv"

# Detecta automáticamente el separador (por si no es coma)
try:
    df = pd.read_csv(file_path)
except Exception:
    df = pd.read_csv(file_path, sep=';')

# === 2. Ver información básica ===
print(" Dimensiones del dataset:", df.shape)
print("\n Columnas:")
print(df.columns.tolist())

# === 3. Mostrar muestra aleatoria ===
print("\n Muestra aleatoria de 10 filas:")
print(df.sample(10, random_state=42))

# === 4. (Opcional) Resumen estadístico de columnas numéricas ===
print("\n Resumen estadístico:")
print(df.describe())

# === 5. (Opcional) Tipos de datos y valores nulos ===
print("\n Información general:")
print(df.info())
