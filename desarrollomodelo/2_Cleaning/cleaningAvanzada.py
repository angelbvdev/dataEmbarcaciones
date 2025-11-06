import pandas as pd
import numpy as np

df = pd.read_csv("embarcaciones_enero_junio_limpio.csv")

# --- 1. Unificación de categorías duplicadas ---
# Normalizar texto a minúsculas y quitar espacios
df['bandera'] = df['bandera'].str.strip().str.lower()
df['tipo_embarcacion'] = df['tipo_embarcacion'].str.strip().str.lower()

# Mapeos de unificación
bandera_map = {
    'panama': 'panamá',
    'mexico': 'mexicana',
}
tipo_map = {
    'car carrier': 'car-carrier',
    'car-carrier': 'car-carrier',
    'containero': 'contenedor',
}

df['bandera'] = df['bandera'].replace(bandera_map)
df['tipo_embarcacion'] = df['tipo_embarcacion'].replace(tipo_map)

# --- 2. Corrección de categorías incorrectas ---
# "panama" como tipo de embarcación → mover a bandera o eliminar
mask_panama_tipo = df['tipo_embarcacion'].str.contains('panama', case=False, na=False)
if mask_panama_tipo.sum() > 0:
    print(f"Corrigiendo {mask_panama_tipo.sum()} registros con tipo_embarcacion = 'panama'")
    # Si no hay tipo correcto disponible, los eliminamos (mejor opción si no hay contexto)
    df = df[~mask_panama_tipo]

# --- 3. Valores imposibles / atípicos ---
# Calado máximo fuera de rango (ej. >20 m probablemente error)
mask_calado = df['calado_maximo'] > 20
if mask_calado.sum() > 0:
    print(f"Eliminando {mask_calado.sum()} registros con calado_maximo > 20 m (probablemente errores)")
    df = df[~mask_calado]

# Horas extremadamente altas — verificar razonabilidad
def limitar_valores(df, col, max_val):
    outliers = df[df[col] > max_val]
    if len(outliers) > 0:
        print(f"{len(outliers)} valores atípicos en {col} eliminados (> {max_val})")
        return df[df[col] <= max_val]
    return df

df = limitar_valores(df, 'horas_buque_puerto', 500)
df = limitar_valores(df, 'horas_buque_operacion', 400)

# --- 4. Anomalía de junio (investigación, no limpieza automática) ---
# Te mostramos el promedio de horas por mes para revisar visualmente
if 'mes' in df.columns:
    resumen_meses = df.groupby('mes')[['horas_buque_operacion']].mean().round(2)
    print("\nPromedio de horas de operación por mes:")
    print(resumen_meses)

# --- 5. Guardar dataset limpio ---
df.to_csv("embarcaciones_limpio.csv", index=False)
print(f"\nDataset limpio guardado con {len(df)} registros.")
