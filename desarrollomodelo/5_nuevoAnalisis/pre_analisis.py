import pandas as pd

# Cargar el dataset combinado
df = pd.read_csv("embarcaciones_comercial.csv")

# === INFORMACIÓN GENERAL ===
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}\n")
print("Columnas disponibles:")
print(df.columns.tolist(), "\n")

print("=== ESTRUCTURA DEL DATAFRAME ===")
print(df.info())

# === LIMPIEZA DE FECHAS ===
# Convertir columnas de fechas si existen
for col in ["fecha_hora_arribo", "fecha_hora_zarpe"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# === DESCRIPCIÓN ESTADÍSTICA ===
print("\n=== DESCRIPCIÓN ESTADÍSTICA ===")
try:
    print(df.describe(include='all', datetime_is_numeric=True))
except TypeError:
    print(df.describe(include='all'))

# === VALORES NULOS ===
print("\n=== VALORES NULOS POR COLUMNA ===")
print(df.isnull().sum().sort_values(ascending=False))

# === ANÁLISIS DE CATEGORÍAS ===
print("\n=== DISTRIBUCIÓN POR BANDERA ===")
print(df["bandera"].value_counts().head(10))

print("\n=== DISTRIBUCIÓN POR TIPO DE EMBARCACIÓN ===")
print(df["tipo_embarcacion"].value_counts().head(10))

print("\n=== DISTRIBUCIÓN POR CAUSA DE ARRIBO ===")
print(df["causa_arribo"].value_counts().head(10))

# === ANÁLISIS DE TONELADAS ===
if "toneladas" in df.columns:
    print("\n=== ESTADÍSTICAS DE TONELADAS ===")
    print(df["toneladas"].describe())
    print("Top 10 embarcaciones por tonelaje:")
    print(df.nlargest(10, "toneladas")[["nombre_buque", "toneladas", "bandera", "tipo_embarcacion"]])

# === ANÁLISIS TEMPORAL ===
if "mes" in df.columns:
    print("\n=== REGISTROS POR MES ===")
    print(df["mes"].value_counts())

# === CORRELACIÓN NUMÉRICA ===
print("\n=== CORRELACIÓN ENTRE VARIABLES NUMÉRICAS ===")
num_cols = df.select_dtypes(include=["float64", "int64"]).columns
print(df[num_cols].corr())

# === EXPORTAR RESUMEN A CSV ===
summary = {
    "total_registros": len(df),
    "columnas": len(df.columns),
    "columnas_con_nulos": df.isnull().sum()[df.isnull().sum() > 0].to_dict(),
    "banderas_top": df["bandera"].value_counts().head(5).to_dict(),
    "tipos_embarcacion_top": df["tipo_embarcacion"].value_counts().head(5).to_dict(),
}
pd.DataFrame([summary]).to_csv("resumen_embarcaciones.csv", index=False)

print("\nAnálisis completo guardado en 'resumen_embarcaciones.csv'")
