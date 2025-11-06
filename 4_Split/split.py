import pandas as pd

# Cargar el dataset original limpio
df = pd.read_csv("embarcaciones_limpio.csv")

# Filtrar los atuneros
if "tipo_embarcacion" in df.columns:
    total_antes = len(df)
    df = df[~df["tipo_embarcacion"].str.lower().str.contains("atunero", na=False)]
    print(f"Registros eliminados (atuneros): {total_antes - len(df)}")
    print(f"Total restante: {len(df)}")
else:
    print("⚠️ La columna 'tipo_embarcacion' no existe en el dataset.")

# Guardar el nuevo dataset (sin atuneros)
output_file = "embarcaciones_comercial_limpio.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Archivo final guardado: {output_file}")
print(f"Total de registros finales: {len(df)}")
print(f"Columnas: {len(df.columns)}")
