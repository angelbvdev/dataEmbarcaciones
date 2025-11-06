import pandas as pd

# 1. Cargar el dataset combinado
df = pd.read_csv("embarcaciones_enero_junio.csv")

print("Filas iniciales:", len(df))

# 2. Eliminar duplicados
df.drop_duplicates(inplace=True)

# 3. Eliminar espacios en blanco en nombres de columnas
df.columns = df.columns.str.strip().str.lower()

# 4. Eliminar filas completamente vacías
df.dropna(how='all', inplace=True)

# 5. Rellenar valores faltantes en columnas importantes si es necesario
cols_rellenar = ["bandera", "tipo_embarcacion", "causa_arribo", "puerto_anterior", "siguiente_puerto"]
for col in cols_rellenar:
    if col in df.columns:
        df[col] = df[col].fillna("Desconocido")

# 6. Convertir fechas a formato datetime 
for col in ["fecha_hora_arribo", "fecha_hora_zarpe"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# 7. Convertir columnas numéricas
numeric_cols = ["tbr", "eslora", "manga", "calado_maximo", "toneladas",
                "vehiculos", "cajas_20", "cajas_40",
                "horas_buque_puerto", "horas_buque_muelle", "horas_buque_operacion"]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 8. Eliminar filas sin nombre de buque o bandera
if "nombre_buque" in df.columns:
    df = df[df["nombre_buque"].notna() & (df["nombre_buque"].str.strip() != "")]
if "bandera" in df.columns:
    df = df[df["bandera"].notna() & (df["bandera"].str.strip() != "")]

# 9. Reiniciar el índice
df.reset_index(drop=True, inplace=True)

# 10. Guardar el dataset limpio
df.to_csv("embarcaciones_enero_junio_limpio.csv", index=False)

print("Filas finales:", len(df))
print("Dataset limpio guardado como 'embarcaciones_enero_junio_limpio.csv'")
