import pandas as pd
import glob

#  Buscar todos los CSV (ajusta el patrón según tus nombres)
# Ejemplo: "Embarcaciones_ENYE_enero_2025.csv", etc.
files = glob.glob("*_ENYE_*_2025.csv")

print(" Archivos encontrados:", files)

#2️ Combinar todos los archivos
df_list = []
for file in files:
    temp = pd.read_csv(file)
    df_list.append(temp)

# Unir todos en un solo DataFrame
df = pd.concat(df_list, ignore_index=True)

# 3️ Limpieza básica
df.drop_duplicates(inplace=True)

# Asegurar que las columnas de mes y año existan
if "mes" not in df.columns:
    df["mes"] = "desconocido"
if "anio" not in df.columns:
    df["anio"] = 2025

# 4️ Guardar dataset combinado
df.to_csv("embarcaciones_enero_junio.csv", index=False)
print(f"\n Dataset combinado guardado como 'embarcaciones_enero_junio.csv'")
print(f" Total de filas: {len(df)}, columnas: {len(df.columns)}")

# 5️ Mostrar resumen rápido
print("\n Columnas disponibles:")
print(df.columns.tolist())

if "mes" in df.columns:
    print("\n Registros por mes:")
    print(df["mes"].value_counts())
