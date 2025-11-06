import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid", palette="muted")

# === 1. Cargar datos ===
df = pd.read_csv("embarcaciones_limpio.csv")

# Conversión de fechas
for col in ["fecha_hora_arribo", "fecha_hora_zarpe"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# === 2. Detección de outliers numéricos (usando IQR) ===
def detectar_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series[(series < lower) | (series > upper)]

outlier_cols = ["toneladas", "eslora", "calado_maximo", "horas_buque_puerto", "horas_buque_operacion"]
outliers_info = {}

for col in outlier_cols:
    if col in df.columns:
        outliers = detectar_outliers(df[col].dropna())
        outliers_info[col] = len(outliers)

# Guardar resumen de outliers
print("=== OUTLIERS DETECTADOS ===")
for col, n in outliers_info.items():
    print(f"{col}: {n} registros fuera de rango")

# === 3. Visualización de outliers por variable ===
for col in outlier_cols:
    if col in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, y=col)
        plt.title(f"Distribución y Outliers - {col}")
        plt.tight_layout()
        plt.savefig(f"boxplot_{col}.png")
        plt.close()

# === 4. Perfiles promedio por tipo de embarcación ===
cols_interes = ["toneladas", "eslora", "calado_maximo", "horas_buque_puerto", "horas_buque_operacion"]

perfil_tipo = (
    df.groupby("tipo_embarcacion")[cols_interes]
    .mean()
    .round(2)
    .sort_values(by="toneladas", ascending=False)
)

perfil_tipo.to_csv("perfil_por_tipo.csv")
print("\nPerfil promedio por tipo de embarcación guardado en 'perfil_por_tipo.csv'")

# === 5. Comparación visual de tonelaje por tipo ===
if "toneladas" in df.columns:
    top_tipos = df["tipo_embarcacion"].value_counts().head(8).index
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=df[df["tipo_embarcacion"].isin(top_tipos)],
        x="tipo_embarcacion",
        y="toneladas"
    )
    plt.xticks(rotation=45, ha="right")
    plt.title("Comparación de Tonelaje entre Tipos de Embarcación (Top 8)")
    plt.tight_layout()
    plt.savefig("comparacion_tonelaje_tipos.png")
    plt.close()

# === 6. Resumen general del análisis ===
resumen = {
    "total_registros": len(df),
    "columnas": len(df.columns),
    "outliers_detectados": outliers_info,
    "tipos_embarcacion": df["tipo_embarcacion"].nunique(),
    "banderas": df["bandera"].nunique(),
    "meses": df["mes"].unique().tolist() if "mes" in df.columns else None
}

pd.Series(resumen).to_json("resumen_analisis.json", indent=4)
print("\nResumen del análisis guardado en 'resumen_analisis.json'")

print("\nGráficas generadas:")
print(" - boxplot_toneladas.png, boxplot_eslora.png, boxplot_calado_maximo.png, etc.")
print(" - comparacion_tonelaje_tipos.png")
