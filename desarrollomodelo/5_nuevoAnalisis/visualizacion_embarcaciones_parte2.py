import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
sns.set(style="whitegrid", palette="deep")

# Cargar el dataset combinado
df = pd.read_csv("embarcaciones_comercial.csv")

# Convertir fechas a datetime
for col in ["fecha_hora_arribo", "fecha_hora_zarpe"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# ===============================
# 1. Correlación entre variables numéricas
# ===============================
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
corr = df[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Matriz de Correlación entre Variables Numéricas")
plt.tight_layout()
plt.savefig("grafica_correlaciones.png")
plt.close()

# ===============================
# 2. Relación entre eslora y tonelaje
# ===============================
if "eslora" in df.columns and "toneladas" in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="eslora", y="toneladas", hue="tipo_embarcacion", alpha=0.7)
    plt.title("Relación entre Eslora y Tonelaje")
    plt.xlabel("Eslora (m)")
    plt.ylabel("Toneladas")
    plt.legend(title="Tipo de embarcación", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("grafica_eslora_tonelaje.png")
    plt.close()

# ===============================
# 3. Tiempo en puerto por tipo de embarcación
# ===============================
if "horas_buque_puerto" in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="tipo_embarcacion", y="horas_buque_puerto")
    plt.xticks(rotation=45, ha="right")
    plt.title("Distribución de Horas en Puerto por Tipo de Embarcación")
    plt.xlabel("Tipo de embarcación")
    plt.ylabel("Horas en puerto")
    plt.tight_layout()
    plt.savefig("grafica_horas_puerto_tipo.png")
    plt.close()

# ===============================
# 4. Tiempos promedio de operación por mes
# ===============================
if {"mes", "horas_buque_operacion"}.issubset(df.columns):
    # Normalizar texto de los meses
    df["mes"] = df["mes"].astype(str).str.strip().str.capitalize()

    # Orden cronológico correcto
    orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

    # Calcular promedio por mes con orden
    df_mes = (
        df.groupby("mes", as_index=False)["horas_buque_operacion"]
        .mean()
    )

    # Asegurar el orden cronológico deseado
    df_mes["mes"] = pd.Categorical(df_mes["mes"], categories=orden_meses, ordered=True)
    df_mes = df_mes.sort_values("mes")

    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=df_mes,
        x="mes",
        y="horas_buque_operacion",
        marker="o",
        color="steelblue"
    )
    plt.title("Promedio de Horas de Operación por Mes (Ene-Jun 2025)")
    plt.xlabel("Mes")
    plt.ylabel("Horas promedio")
    plt.tight_layout()
    plt.savefig("grafica_operacion_mes.png")
    plt.close()


# ===============================
# 5. Relación entre tonelaje y calado máximo
# ===============================
if {"toneladas", "calado_maximo"}.issubset(df.columns):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, x="calado_maximo", y="toneladas",
        hue="bandera", alpha=0.7, palette="tab10"
    )
    plt.title("Relación entre Tonelaje y Calado Máximo por Bandera")
    plt.xlabel("Calado máximo (m)")
    plt.ylabel("Toneladas")
    plt.legend(title="Bandera", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("grafica_calado_tonelaje.png")
    plt.close()

print("Gráficas avanzadas generadas y guardadas como:")
print(" - grafica_correlaciones.png")
print(" - grafica_eslora_tonelaje.png")
print(" - grafica_horas_puerto_tipo.png")
print(" - grafica_operacion_mes.png")
print(" - grafica_calado_tonelaje.png")
