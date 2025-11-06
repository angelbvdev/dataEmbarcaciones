import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general de estilo
sns.set(style="whitegrid", palette="muted")

# Cargar el dataset combinado
df = pd.read_csv("embarcaciones_limpio.csv")

# Convertir fechas
for col in ["fecha_hora_arribo", "fecha_hora_zarpe"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# === 1. Distribución de banderas ===
top_banderas = df["bandera"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_banderas.values, y=top_banderas.index)
plt.title("Top 10 Banderas de Embarcaciones (Ene-Jun 2025)")
plt.xlabel("Cantidad de embarcaciones")
plt.ylabel("Bandera")
plt.tight_layout()
plt.savefig("grafica_banderas.png")
plt.close()

# === 2. Distribución por tipo de embarcación ===
top_tipos = df["tipo_embarcacion"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_tipos.values, y=top_tipos.index, color="skyblue")
plt.title("Tipos de Embarcación más Comunes")
plt.xlabel("Cantidad")
plt.ylabel("Tipo de embarcación")
plt.tight_layout()
plt.savefig("grafica_tipos_embarcacion.png")
plt.close()

# === 3. Tonelaje promedio por tipo de embarcación ===
if "toneladas" in df.columns:
    ton_por_tipo = df.groupby("tipo_embarcacion")["toneladas"].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=ton_por_tipo.values, y=ton_por_tipo.index, color="salmon")
    plt.title("Tonelaje Promedio por Tipo de Embarcación")
    plt.xlabel("Toneladas promedio")
    plt.ylabel("Tipo de embarcación")
    plt.tight_layout()
    plt.savefig("grafica_tonelaje_tipo.png")
    plt.close()

# === 4. Tonelaje promedio por bandera ===
ton_por_bandera = df.groupby("bandera")["toneladas"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=ton_por_bandera.values, y=ton_por_bandera.index, color="lightgreen")
plt.title("Tonelaje Promedio por Bandera")
plt.xlabel("Toneladas promedio")
plt.ylabel("Bandera")
plt.tight_layout()
plt.savefig("grafica_tonelaje_bandera.png")
plt.close()

# === 5. Arribos por mes ===
if "mes" in df.columns:
    # Asegurar que la columna 'mes' esté en formato texto consistente
    df["mes"] = df["mes"].astype(str).str.strip().str.capitalize()

    # Orden correcto de los meses (ajústalo según tus datos)
    orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="mes",
        order=orden_meses,
        color="skyblue"
    )
    plt.title("Cantidad de Arribos por Mes (Ene-Jun 2025)")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de registros")
    plt.tight_layout()
    plt.savefig("grafica_arribos_mes.png")
    plt.close()


print("Gráficas generadas y guardadas como archivos PNG:")
print(" - grafica_banderas.png")
print(" - grafica_tipos_embarcacion.png")
print(" - grafica_tonelaje_tipo.png")
print(" - grafica_tonelaje_bandera.png")
print(" - grafica_arribos_mes.png")
